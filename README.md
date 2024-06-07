# easy-figlet

Deal with figlet easily. Basically a wrapper.

# Setup

This guide is written for Windows users.

1. [Click here](https://github.com/hirusha-adi/easy-figlet/archive/refs/heads/main.zip) to download the source code in the master branch of this github repository.

2. Extract it and cd into it

3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

4. Run the script

```bash
python easy-figlet.py
```

# Usage

## Command Usage

```
>python easy-figlet.py --help
usage: easy-figlet.py [-h] [--font FONT] [--list] [-r] [-u] [-l] [-s [SAVE]] [text]

Generate ASCII art with pyfiglet.

positional arguments:
  text                  Text to convert to ASCII art

options:
  -h, --help            show this help message and exit
  --font FONT           Font to use for the ASCII art
  --list                List all available fonts
  -r, --random          Print text with a random font
  -u, --uppercase       Convert text to uppercase
  -l, --lowercase       Convert text to lowercase
  -s [SAVE], --save [SAVE]
                        Save the result to a file
```

## Examples

```bash
python easy-figlet.py --help
python easy-figlet.py "hirusha"
python easy-figlet.py "hirusha" --font standard
python easy-figlet.py "hirusha" --random
python easy-figlet.py "hirusha" -u
python easy-figlet.py "hirusha" -l
python easy-figlet.py "hirusha" -s
python easy-figlet.py "hirusha" -s "file.txt"
```
