> [!IMPORTANT]
> This project has been archived. Check out the rewrite I'm working on here: [PigLatin+](https://gitlab.com/thecasualdev/piglatin)

# Pig Latin Translator

This is a simple Pig Latin translator the I created for school.

## To-Do List

- [x] Create Pig Latin Translator
- [x] Custom draw module to allow for simple, yet consitance outputs
- [x] Config reading and generating
- [x] Simple module to toggle Y checking (allows the script to differentiate between Y as a vowel & Y as a consonant)
- [x] Output file, or custom destination
- [x] Way to seperate main symbols from text (semi-support, just ignores all other characters)
- [x] Option to generate new file within the same directory
- [x] Console menu

## Setup

> [!NOTE]
> Though not required as the project is built only using internal packages.
> It is recomended to setup a virtual environment using the [venv](https://docs.python.org/3/library/venv.html) module.

Next you will want to make sure you are running python ``3.9`` minimum
With the adition of the new ``piglatin.cmd`` you can simply add the directory path
And run the program simply by running ``piglatin``

## Usage

If you have setup path simply run

```bash
piglatin
```

if you don't have it on path simply CD into the directory
And then run

``` bash
py piglatin.py
```

Below are the flags you can run the application with.

``` bash
  -h, --help            show this help message and exit
  -S STRING, --string STRING
                        Used to translate a single string
  -F FILE, --file FILE  Used to translate entire files, only supports .txt
  -y, --ycheck, --no-ycheck
                        Toggle the function that differentiates between Y as a vowel & Y as a consonant
  -o OUTPUT, --output OUTPUT
                        Set a unique output location (used for translating files)
  -s, --setup           Used to generate defualt config file and output folder
  -k, --keepd, --no-keepd
                        Quick argument to create new file in the same directory as input txt file
```
