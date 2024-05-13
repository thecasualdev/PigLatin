
# This is the main script of the 

from . import draw, settings, translate

import argparse
import os

# Setups the argument parser, allowing for instant use of the tool without using menus

parser = argparse.ArgumentParser(
    prog="Pig Latin Translator",
    description="Semi-Advanced, overcomplicated pig latin translator"
)

parser.add_argument('-S', '--string', help="Used to translate a single string")
parser.add_argument('-F', '--file', help="Used to translate entire files, only supports .txt")
parser.add_argument('-y', '--ycheck', action=argparse.BooleanOptionalAction, help="Toggle the function that differentiates between Y as a vowel & Y as a consonant")
parser.add_argument('-o', '--output', help="Set a unique output location (used for translating files)")
parser.add_argument('-s', '--setup', help="Used to generate defualt config file and output folder", action="store_true")
parser.add_argument('-k', '--keepd', action=argparse.BooleanOptionalAction, help="Quick argument to create new file in the same directory as input txt file")

config = settings.load_config()
args = parser.parse_args()

y_check = args.ycheck or config.getboolean('general', 'y_check')
keep_d = args.keepd or config.getboolean('output', 'keep-directory')
auto_run = config.getboolean('general', 'auto_run')

def string_menu():
    draw.text_output("Input the string that you wish to translate [type 0 to exit]")
    input = str(draw.text_input("String"))

    if input == "0":
        draw.text_output("Closing application...")
        exit()
    
    draw.text_output("Translating string...")
    draw.text_output(f"Translated string '{translate.string(input, False, False)}'")

    if config.getboolean('general', 'auto_run'):
        string_menu()
    
    else:
    
        check = str.lower(draw.text_input("Do you wish to run again? [y/n]"))
        if check in ['y', 'yes', 'true']:
            string_menu()
        
        else:
            draw.text_output("Closing application...")
            exit()

def file_menu(lkd):

    local_keep_d:bool = lkd

    draw.text_output(f"Select from following options : 1) Input File, 2) Toggle Same Directory [{local_keep_d}], 3) Exit")
    option = str.lower(draw.text_input("Select option"))

    if option in ["input", "input file", "1", "i"]:

        result = translate.file(args.file, args.output, y_check, local_keep_d)
        draw.text_output("Translation and can be found at ::" + result.name)

        if config.getboolean('general', 'auto_run'):
            file_menu(local_keep_d)
            
        else:
    
            check = str.lower(draw.text_input("Do you wish to run again? [y/n]"))
            if check in ['y', 'yes', 'true']:
                string_menu()
            
            else:
                draw.text_output("Closing application...")
                exit()
        
    elif option in ["toggle", "toggle same directory", "2", "t"]:

        if local_keep_d:
            local_keep_d = False
            file_menu(local_keep_d)

        else:
            local_keep_d = True
            file_menu(local_keep_d)
        
    elif option in ["exit", "close", "3", "e"]:
        draw.text_output("Closing application...")
        exit()


class app:

    if args.setup:
        draw.text_output("Generating defualt files...")
        settings.generate_config()
        exit()
    
    # Safe argument checker, closes the application if 

    if args.string and args.file:
        draw.text_output("You can not translate strings and files at the same time")
        draw.text_output("write `-h` to learn more about arguments")
        exit()

    if args.output and not args.file:
        draw.text_output("The output argument requires the file argument")
        draw.text_output("write `-h` to learn more about arguments")
        exit()
    
    if args.keepd and not args.file:
        draw.text_output("The keep directory argument requires the file argument")
        draw.text_output("write `-h` to learn more about arguments")
        exit()

    if args.ycheck:
        if not args.string:
            if not args.file:
                draw.text_output("The `Y Check` argument requires either the file or string argument")
                draw.text_output("write `-h` to learn more about arguments")
                exit()

    output = args.string or args.file or "test"

    if args.string:

        if y_check:
            draw.text_output("Starting translation [with Y checking]")
        else:
            draw.text_output("Starting translation")

        result = translate.string(args.string, y_check, True)
        draw.text_output("Translation completed :: " + result)
        exit()
    
    if args.file:

        if y_check:
            draw.text_output("Starting translation of " + args.file + " [with Y checking]")
        else:
            draw.text_output("Starting translation" + args.file)

        result = translate.file(args.file, args.output, y_check, keep_d)
        draw.text_output("Translation and can be found at ::" + result.name)
        exit()

    def main_menu():
        
        draw.text_output("Welcome to the most simple yet overengineered translator")
        draw.text_output("By Jack M.")

        print()

        draw.text_output("Please select from the following options : 1) String Translate, 2) File Translate, 3) Exit")
        option = str.lower(draw.text_input("Select option"))

        if option in ["string", "string translate", "1", "s"]:
            string_menu()
        
        elif option in ["file", "file translate", "2", "f"]:
            file_menu(keep_d)
        
        elif option in ["exit", "close", "3", "e"]:
            draw.text_output("Closing application...")
            exit()
        
        else:
            draw.text_output("Not valid input")
            exit()            

    draw.text_output("Loading menu...")
    
    if config.getboolean('general', 'clean_terminal'):
        os.system('cls' if os.name == 'nt' else 'clear')

    print()

    draw.title("pig latin translator")

    main_menu()