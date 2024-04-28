
# This is the main translate file for the application
# Created by TheCasualDev
# v 1.0

from . import draw

import time
import os

vowels = ['a', 'e', 'i', 'o', 'u']

def ychecker(input):
    print(input)

def string(input:str, y_check:bool):

    start_time = time.time()

    result = []
    sentance = input.split(" ")
    
    draw.progress_bar(0, len(sentance))

    for index, word in enumerate(sentance):
    
        draw.progress_bar(index + 1, len(sentance))

        has_vowel = False

        for index in range(len(word)):
            
            if word[0] in vowels:
                result.append(word + 'ay')
                break
            
            else:

                if word[index] in vowels:
                    result.append(word[index:] + word[:index] + 'ay')
                    has_vowel = True
                    break

                if (has_vowel == False and index == len(word)-1):
                    result.append(word + 'ay')

    draw.text_output("Translated string in " + str(time.time() - start_time) + "ms")
    return str.capitalize(' '.join(result))

def document(input:str, y_check:bool):

    start_time = time.time()

    result = ""

    return result