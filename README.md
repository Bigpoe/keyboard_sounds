## Description

This is a simple Python application to play a .mp3 file when a letter key is pressed in the keyboard.

## Quick Start

1. Download the repository.
2. Open a new terminal.
3. (OPTIONAL) Create a Python virtual environment with [venv](https://docs.python.org/3/tutorial/venv.html) or [pyenv](https://pypi.org/project/pyvenv/) and activate.


## Usage

*Add audio files (tested on .mp3 files)*

1. Add the .mp3 files you want to use in `keyboard_sounds/media/sounds` folder.
2. Open `keyboard_sounds/scripts/config/sounds_list.py` and make sure the audio file name corresponds to the desired letter. You can check the included examples.

*Unix base system instructions*

1. Install dependencies with `pip3 install -r requirements.txt`.
2. Run the application for Unix base operative systems with `sudo python keyboard_sounds/`.

*Windows instructions*
1. Install dependencies with `pip3 install -r windows_requirements.txt`.
2. Run the application for Unix base operative systems with `sudo python keyboard_sounds/`.

*Stop the application*

If you need to stop the application, go to the terminal where you executed the application and stop it pressing `control + c`.
