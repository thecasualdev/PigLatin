
# This is the main script of the 

from . import draw, setup

import argparse

# Setups the argument parser, allowing for instant use of the tool without using menus

parser = argparse.ArgumentParser(
    prog="Pig Latin Translator",
    description="Semi-Advanced, overcomplicated pig latin translator"
)

parser.add_argument('-S', '--string', help="Used to translate a single string")
parser.add_argument('-F', '--file', help="Used to translate entire files, only supports .txt")
parser.add_argument('-y', '--ycheck', help="Toggle the function that differentiates between Y as a vowel & Y as a consonant")
parser.add_argument('-o', '--output', help="Set a unique output location (used for translating files)")
parser.add_argument('-s', '--setup', help="Used to generate defualt config file and output folder", action="store_true")

class app:

    args = parser.parse_args()

    if args.setup:
        draw.text_output("Generating defualt files...")
        setup.generate_config()
        exit()

    print("Howdy")