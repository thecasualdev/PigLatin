
# This is a simple module that stores some basic drawing functions for the CLI
# I might not be able to make it a GUI or use Colorama but it sure as hell will look pretty.

def text_output (content) :
    print ("# " + str(content))

def text_input (content:str) :
    value = input("# " + str(content) + " > ") 
    return value

def progress_bar (progress, total) :
    percent = 100 * (progress / float(total)) 
    bar = '▮' * int(percent) + '▯' * (100 - int(percent)) 
    print(f"\r# [{bar}] {int(percent)}%", end='\r')