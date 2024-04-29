
# Used for generating the defualt output folder and config

from . import draw

import os
import time
import configparser

config = configparser.ConfigParser()

def generate_config():
    
    start_time = time.time()
    
    if not os.path.exists('./output'):
        os.mkdir('./output')

    config.add_section("general")
    config.add_section("output")

    config.set("general", "y_check", "True")
    config.set("general", "auto_run", "True") 
    config.set("output", "directory", "./output")
    config.set("output", "keep-directory", "False")

    with open("config.init", 'w') as file:
        config.write(file)

    draw.text_output("Generated defualt files in " + str(time.time() - start_time) + "ms")

def load_config():

    if os.path.exists('./config.init'):
        config.read('./config.init')
        
    else:

        draw.text_output("No config found")
        
        check = str.lower(draw.text_input("Do you wish to run config generator? [y/n]"))

        if check in ['y', 'yes', 'true']:
            draw.text_output("Generating defualt files")
            generate_config()
            draw.text_output("Setup completed, you can now run `py piglatin.py` again")
            exit()

        exit()

    return config