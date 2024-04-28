
# This is the main translate file for the application
# Created by TheCasualDev (Jack M.)
# v2.0

from . import draw

import time
import os
import re

vowels = ['a', 'e', 'i', 'o', 'u']

def string(input:str, y_check:bool):

    # Runs at the start of the function, creating a checkpoint for current time and a empty list
    start_time = time.time()
    result = []

    # Splits the string into a list, seperating the result with the regular expression operator
    sentance = re.findall(r'\w+', input) # w checks for alphanumeric characters

