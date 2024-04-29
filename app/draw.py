
# This is a simple module that stores some basic drawing functions for the CLI
# I might not be able to make it a GUI or use Colorama but it sure as hell will look pretty.

def text_output (content) :
    print (f"# {str(content)}")

def text_input (content) :
    value = input(f"# {str(content)} > ") 
    return value

def title (content) :
    title = ("│     " + str.title(content) + "     │") 
    print("┌" + "―" * int(len(title) - 2) + "┐")
    print(title)
    print("└" + "―" * int(len(title) - 2) + "┘")
    print()

def progress_bar (progress, total) :

    percent = 100 * (progress / float(total)) 
    bar = '▮' * int(percent) + '▯' * (100 - int(percent))

    print(f"\r# [{bar}] {int(percent)}%", end='\r')

    if progress == total :
        print(f"\r# [{bar}] {int(percent)}% DONE!!")