
# Used for generating the defualt output folder and config

from . import draw

import os
import time

def generate_config():
    
    start_time = time.time()
    
    if not os.path.exists('./output'):
        os.mkdir('./output')

    config = open('./.config', '+w')

    config.write("output='./output'" + '\n')
    config.write("ycheck=true" + '\n')

    config.close()

    draw.text_output("Generated defualt files in " + str(time.time() - start_time) + "ms")