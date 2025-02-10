# ASCII Art Generator

This Python script allows you to generate ASCII art from text, customize the font, and save the result to a file. You can list available fonts, convert text to uppercase or lowercase, or use a random font.

## Requirements

- Run the command below to install the required python libraries:

```
python -m pip install -r requirements.txt
```

## Usage

### Basic Usage
To generate ASCII art from a provided text:

```bash
python ascii_art_generator.py "Hello World"
```

### Options

- `--font` (optional): Specify the font to use for generating the ASCII art.
  
  Example:
  ```bash
  python ascii_art_generator.py "Hello World" --font "slant"
  ```

- `--list` or `--list-fonts`: List all available fonts.

  Example:
  ```bash
  python ascii_art_generator.py --list
  ```

- `-r` or `--random`: Generate ASCII art with a random font.

  Example:
  ```bash
  python ascii_art_generator.py "Hello World" -r
  ```

- `-u` or `--uppercase`: Convert the input text to uppercase before generating the ASCII art.

  Example:
  ```bash
  python ascii_art_generator.py "Hello World" -u
  ```

- `-l` or `--lowercase`: Convert the input text to lowercase before generating the ASCII art.

  Example:
  ```bash
  python ascii_art_generator.py "Hello World" -l
  ```

- `-s` or `--save`: Save the generated ASCII art to a file. If no filename is provided, it will save the result with the text as the filename (sanitized).

  Example:
  ```bash
  python ascii_art_generator.py "Hello World" -s output.txt
  ```

  If no filename is provided, the file will be saved as `Hello_World.txt`.

### Example Commands

- Generate ASCII art with the default font:
  ```bash
  python ascii_art_generator.py "Hello World"
  ```

- Generate ASCII art using the "slant" font:
  ```bash
  python ascii_art_generator.py "Hello World" --font "slant"
  ```

- Generate ASCII art using a random font:
  ```bash
  python ascii_art_generator.py "Hello World" -r
  ```

- Save the result to a file named `output.txt`:
  ```bash
  python ascii_art_generator.py "Hello World" -s output.txt
  ```

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.
