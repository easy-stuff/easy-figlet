import sys
import os
import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Generate ASCII art with pyfiglet.')
    parser.add_argument('font', type=str, help='Font to use for the ASCII art')
    parser.add_argument('text', nargs='*', help='Text to convert to ASCII art')

    args = parser.parse_args()

    if not args.text:
        print_help()
        sys.exit()

    text = ' '.join(args.text)
    font = args.font

    all_fonts = pyfiglet.FigletFont.getFonts()

    generate_art(all_fonts=all_fonts, font=font, text=text)

if __name__ == "__main__":
    main()
