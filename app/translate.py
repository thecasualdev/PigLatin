
# This is the main translate file for the application
# Created by TheCasualDev (Jack M.)
# v2.0

from . import draw, settings

import time
import os
import re

def string(input:str, y_check:bool, check_time:bool):

    # Runs at the start of the function, creating a checkpoint for current time and a empty list
    start_time = time.time()
    result = []

    # Splits the string into a list, seperating the result with the regular expression operator
    sentance = re.findall(r'\w+', str.lower(input)) # w checks for alphanumeric characters

    if check_time:
        draw.progress_bar(0, len(sentance))

    # Begins the main loop, using the enumerate object to get a counter
    for i, word in enumerate(sentance):

        if check_time:
            draw.progress_bar(i + 1, len(sentance))

        vowel:bool = False

        # Allows us too loop through a word checking each for the following rules
        #   - Check if the vowel is at the strart of the word, appending 'way' to the end of it
        #   - Iterate through constants  till a vowel is found, which at that 
        #     point move the first constants to the end and add 'ay'
        #   - As fall back if no vowel is found, append 'ay' to the end of it

        for i in range(len(word)):
            
            vowels = ['a', 'e', 'i', 'o', 'u']

            # Checks to see if the first letter contains a vowel, if true adds 'way' then breaks
            if word[0] in vowels:
                result.append(word + 'way')
                break
                
            else:

                # Temporary place holder until I make an actual algorithm
                if y_check:
                    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

                # Checks the current index with the matching letter and compares with with the vowels list
                # Then using the slice syntax splits the word at the point of the vowel
                if word[i] in vowels:
                    result.append(word[i:] + word[:i] + 'ay')
                    vowel = True
                    break

                # Fail safe, if the word dosen't match any of the above rules, adds 'ay' to the end
                if (vowel == False and i == len(word)-1):
                    result.append(word + 'ay')

    if check_time:
        draw.text_output("Translated string in " + str(time.time() - start_time) + "ms")
    
    # Returns the final result as a string
    return str.capitalize(' '.join(result))

def file(input:str, output:str, y_check:bool, keep_d:bool):

    # Runs at the start of the function, creating a checkpoint for current time and a empty list
    start_time = time.time()

    config = settings.load_config()   
    output = output or config.get('output', 'directory')

    # Checks if KeepD is enabled, if so sets directory to the files current directory
    if keep_d:
        output = os.path.dirname(input)

    # First we do some basic checks, veryfying the exsistance of the provided files
    if not os.path.exists(input):
        draw.text_output("File could not be found")
        draw.text_output("Please try again")
        exit()
    
    if not os.path.exists(output):
        draw.text_output("Could not find provided output file")
        if not os.path.exists('./output'):
            draw.text_output("Generating now...")
            os.mkdir('./output')
        exit()

    # Followed with making sure that the file is the correct file type
    file = os.path.basename(input)
    name, extension = os.path.splitext(file)

    name_out = name + "_piglatin"

    if config.getboolean("output", "translate-name"):
        name_out = string(name, y_check, False)
    
    if not extension.lower() == '.txt':
        draw.text_output("File is not supported, please make sure file is a txt")
        exit()

    draw.text_output("Opening file")

    # This begins the sequence by opening the file, and generating the result file to write too
    file_open = open(input, 'r', encoding="utf8")
    file_result = open(output + "/" + name_out + ".txt" , 'w')

    # This will loop through the opened file by sentance (line) and feed it through the preexisting single string function made above.
    # It then writes the result to the file_result file
    for sentance in file_open:
        translated = string(sentance, y_check, False)
        file_result.write(translated + '\n')
    
    draw.text_output("Writing to file")

    # Closes both of the files
    file_open.close()
    file_result.close()

    draw.text_output("Translated file in " + str(time.time() - start_time) + "ms")

    # And returns the directory to the user
    return file_result