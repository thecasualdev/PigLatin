
# This is the main script of the 

from . import draw, settings, translate

import argparse

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

class app:

    args = parser.parse_args()

    if args.setup:
        draw.text_output("Generating defualt files...")
        settings.generate_config()
        exit()

    config = settings.load_config()

    y_check = args.ycheck or config.getboolean('general', 'y_check')
    auto_run = config.getboolean('general', 'auto_run')
    
    # Safe argument checker, closes the application if 

    if args.string and args.file:
        draw.text_output("You can not translate strings and files at the same time")
        draw.text_output("write `-h` to learn more about arguments")
        exit()

    if args.output and not args.file:
        draw.text_output("The output argument requires the file argument")
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

        result = translate.file(args.file, args.output, y_check)
        draw.text_output("Translation and can be found at ::" + result.name)
        exit()

    draw.text_output(output)