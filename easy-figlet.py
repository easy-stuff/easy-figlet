import click
import re
import pyfiglet
from random import choice


def generate_art(font, text):
    return pyfiglet.figlet_format(text, font=font)


def display_fonts():
    fonts = pyfiglet.FigletFont.getFonts()
    for idx, font in enumerate(fonts):
        click.echo(f"{idx} | {font}\n--------------")


def sanitize_filename(text):
    return re.sub(r"[^\w\-_. ]", "_", text) + ".txt"


def save_to_file(content, filename):
    with open(filename, "w") as f:
        f.write(content)


@click.command()
@click.argument("text", required=False)
@click.option("--font", type=str, help="Font to use for the ASCII art.")
@click.option("--list", "--list-fonts", "list_fonts_flag", is_flag=True, help="List all available fonts.")
@click.option("-r", "--random", is_flag=True, help="Print text with a random font.")
@click.option("-u", "--uppercase", is_flag=True, help="Convert text to uppercase.")
@click.option("-l", "--lowercase", is_flag=True, help="Convert text to lowercase.")
@click.option("-s","--save",type=str,default=None,help="Save the result to a file. Provide a filename or it will use the text as the filename.",)
def main(text: str, font: str, list_fonts_flag, random, uppercase, lowercase, save: str):
    if list_fonts_flag: 
        display_fonts()
        return

    if not text:
        click.echo("No text provided. Use --help for more details.")
        return

    if uppercase:
        text = text.upper()
    elif lowercase:
        text = text.lower()

    font = choice(pyfiglet.FigletFont.getFonts()) if random else (font or "standard")
    result = generate_art(font, text)
    click.echo(result)

    if save is not None:
        filename = save if save else sanitize_filename(text)
        save_to_file(result, filename)
        click.echo(f"Output saved to {filename}")


if __name__ == "__main__":
    main()
