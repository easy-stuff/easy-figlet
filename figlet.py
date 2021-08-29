import pyfiglet, sys
from random import choice

# List of all fonts
allfonts = pyfiglet.FigletFont.getFonts()

# Text
try:
    alltext = ' '.join(sys.argv[2:])
except:
    alltext = "ZeaCeR"

# Font
try:
    font = sys.argv[1]
except IndexError:
    font = "help"
    alltext = "ZeaCeR"

def SHIT(allfonts, font, alltext):
    # world lists
    rnd_wl = ("random", "rand", "r", "skip", "any", "no", "dont")
    fonts_wl = ("list", "fonts", "show", "showfonts", "listfonts")

    # Program starts here
    if font.lower() in rnd_wl:
        result = pyfiglet.figlet_format(f"{alltext}", font = f"{choice(allfonts)}" )
        print(result)

    elif font in allfonts: 
        result = pyfiglet.figlet_format(f"{alltext}", font = f"{font}" )
        print(result)

    elif font.lower() in fonts_wl:
        for countx, i in enumerate(allfonts):
            print(f"{countx} | {i}")
            print("--------------")

    else:
        print("""
    ███████╗██╗ ██████╗ ██╗     ███████╗████████╗
    ██╔════╝██║██╔════╝ ██║     ██╔════╝╚══██╔══╝
    █████╗  ██║██║  ███╗██║     █████╗     ██║   
    ██╔══╝  ██║██║   ██║██║     ██╔══╝     ██║   
    ██║     ██║╚██████╔╝███████╗███████╗   ██║   
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
                by ZeaCeR#5641

    Usage:
        figlet [font=random] [text]

    Others:
        figlet help --> Show this
        figlet list --> Show all fonts
        """)

if __name__ == "__main__":
    SHIT(allfonts=allfonts, font=font, alltext=alltext)
