import click
import re
import pyfiglet
from random import choice
from typing import Optional


def generate_art(font: str, text: str) -> str:
    """Generate ASCII art using the given font and text."""
    try:
        return pyfiglet.figlet_format(text, font=font)
    except Exception as e:
        raise ValueError(f"Error generating ASCII art: {e}")


def display_fonts() -> None:
    """Display a list of all available fonts."""
    fonts = pyfiglet.FigletFont.getFonts()
    if not fonts:
        raise RuntimeError("No fonts available.")
    for idx, font in enumerate(fonts):
        click.echo(f"{idx} | {font}\n--------------")


def sanitize_filename(text: str) -> str:
    """Sanitize text to create a valid filename."""
    return re.sub(r"[^\w\-_. ]", "_", text) + ".txt"


def save_to_file(content: str, filename: str) -> None:
    """Save the ASCII art content to a file."""
    try:
        with open(filename, "w") as f:
            f.write(content)
    except OSError as e:
        raise IOError(f"Error saving file {filename}: {e}")


@click.command()
@click.argument("text", required=False)
@click.option("--font", type=str, help="Font to use for the ASCII art.")
@click.option("--list", "--list-fonts", "list_fonts_flag", is_flag=True, help="List all available fonts.")
@click.option("-r", "--random", is_flag=True, help="Print text with a random font.")
@click.option("-u", "--uppercase", is_flag=True, help="Convert text to uppercase.")
@click.option("-l", "--lowercase", is_flag=True, help="Convert text to lowercase.")
@click.option("-s", "--save", type=str, default=None, help="Save the result to a file. Provide a filename or it will use the text as the filename.")
def main(
    text: Optional[str],
    font: Optional[str],
    list_fonts_flag: bool,
    random: bool,
    uppercase: bool,
    lowercase: bool,
    save: Optional[str]
) -> None:
    """Main command for generating ASCII art with optional saving to a file."""
    
    if list_fonts_flag:
        display_fonts()
        return

    if not text:
        click.echo("No text provided. Use --help for more details.")
        return

    # Handle text transformation
    if uppercase:
        text = text.upper()
    elif lowercase:
        text = text.lower()

    # Choose font
    font = choice(pyfiglet.FigletFont.getFonts()) if random else (font or "standard")
    
    # Generate the ASCII art
    try:
        result = generate_art(font, text)
    except ValueError as e:
        click.echo(f"Error: {e}")
        return

    # Display the result
    click.echo(result)

    # Save to file if requested
    if save:
        filename = save if save else sanitize_filename(text)
        try:
            save_to_file(result, filename)
            click.echo(f"Output saved to {filename}")
        except IOError as e:
            click.echo(f"Error saving file: {e}")


if __name__ == "__main__":
    main()
