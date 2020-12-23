import keyboard
from playsound import playsound
from ..config import sounds_list
from ..config import config

# this function is called whenever a key is pressed
def _on_press(event):
    try:
        # constructs the file path of the sound to be played
        sound_file = config.sound_directory + sounds_list.key_sound[event.name]
        playsound(sound_file, not config.async_play)
    except OSError:
        print(f"Sound file '{sound_file}' doesn't exist")
    except KeyError:
        print(f"'{event.name}' key not configured")

def read_inputs():
    # create a global listener for a KEY_DOWN event
    keyboard.on_press(_on_press)

    # infinite loop
    while True:
        None
