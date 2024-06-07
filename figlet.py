import sys
import os

try:
    import pyfiglet
except ImportError:
    os.system(f"{'pip' if os.name == 'nt' else 'pip3'} install pyfiglet")
    import pyfiglet

from random import choice

def print_help():
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

all_fonts = pyfiglet.FigletFont.getFonts()

# Text
try:
    text = ' '.join(sys.argv[2:])
except IndexError:
    print_help()
    sys.exit()

# Font
try:
    font = sys.argv[1]
except IndexError:
    print_help()
    sys.exit()


def generate_art(all_fonts, font, text):
    # Word lists
    random_font_triggers = ("random", "rand", "r", "skip", "any", "no", "dont")
    font_list_triggers = ("list", "fonts", "show", "showfonts", "listfonts")

    # Program starts here
    if font.lower() in random_font_triggers:
        result = pyfiglet.figlet_format(text, font=choice(all_fonts))
        print(result)
    elif font in all_fonts:
        result = pyfiglet.figlet_format(text, font=font)
        print(result)
    elif font.lower() in font_list_triggers:
        for idx, fnt in enumerate(all_fonts):
            print(f"{idx} | {fnt}")
            print("--------------")
    else:
        print_help()

if __name__ == "__main__":
    generate_art(all_fonts=all_fonts, font=font, text=text)
