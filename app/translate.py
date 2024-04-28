
# This is the main translate file for the application
# Created by TheCasualDev (Jack M.)
# v2.0

from . import draw

import time
import os
import re

def string(input:str, y_check:bool, check_time:bool):

    # Runs at the start of the function, creating a checkpoint for current time and a empty list
    start_time = time.time()
    result = []

    # Splits the string into a list, seperating the result with the regular expression operator
    sentance = re.findall(r'\w+', str.lower(input)) # w checks for alphanumeric characters

    draw.progress_bar(0, len(sentance))

    # Begins the main loop, using the enumerate object to get a counter
    for i, word in enumerate(sentance):

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
    
    return str.capitalize(' '.join(result))