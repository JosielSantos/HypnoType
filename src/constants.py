import os

APPLICATION_DIRECTORY = os.path.join(os.path.expanduser("~"), ".hypno-type")
EXPANSIONS_FILE = os.path.join(APPLICATION_DIRECTORY, "expansions.json")
SOUNDS_DIRECTORY = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))) + '/sounds'
