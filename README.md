# easy-figlet

Deal with figlet easily. Basically a wrapper.

# Setup

## Run from source

This installation guide is written for Windows users.

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

# Compiling

1. Setup a virtual environment
```bash
python -m venv env
```

2. Use that virtual environment
```bash
.\env\Scripts\activate.bat
```

3. Install requirements
```bash
python3 -m pip -r requirements.txt
```

4. Install PyInstaller to build the file
```bash
python -m pip install PyInstaller
```

5. Compile
```bash
python -m PyInstaller easy-figlet.py --name "easy-figlet" --icon "logo.ico" --onefile --console --noconfirm
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
