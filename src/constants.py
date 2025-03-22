import os

APPLICATION_USER_DIRECTORY = os.path.join(
    os.path.expanduser("~"), ".hypnotype")
SHORTCUTS_FILE = os.path.join(APPLICATION_USER_DIRECTORY, "shortcuts.json")
SOUNDS_DIRECTORY = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
) + '/sounds'

if not os.path.exists(APPLICATION_USER_DIRECTORY):
    os.makedirs(APPLICATION_USER_DIRECTORY)
