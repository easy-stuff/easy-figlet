import sys
import os
import argparse
from random import choice
import pyfiglet

def generate_art(font, text):
    result = pyfiglet.figlet_format(text, font=font)
    print(result)

def list_fonts():
    fonts = pyfiglet.FigletFont.getFonts()
    for idx, font in enumerate(fonts):
        print(f"{idx} | {font}")
        print("--------------")

def main():
    parser = argparse.ArgumentParser(description='Generate ASCII art with pyfiglet.')
    parser.add_argument('text', nargs='?', help='Text to convert to ASCII art')
    parser.add_argument('--font', type=str, help='Font to use for the ASCII art')
    parser.add_argument('--list', action='store_true', help='List all available fonts')
    parser.add_argument('-r', '--random', action='store_true', help='Print text with a random font')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Convert text to uppercase')
    parser.add_argument('-l', '--lowercase', action='store_true', help='Convert text to lowercase')

    args = parser.parse_args()

    if args.list:
        list_fonts()

    if args.text is None:
        print("No text passed in as an argument. Please use --help to learn more.")
        sys.exit()

    text = args.text
    if args.uppercase:
        text = text.upper()
    elif args.lowercase:
        text = text.lower()

    if args.random:
        font = choice(pyfiglet.FigletFont.getFonts())
    else:
        font = args.font if args.font else 'standard'

    generate_art(font, text)

if __name__ == "__main__":
    main()
