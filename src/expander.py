import keyboard
import pyperclip
import pyautogui
import threading
from config import load_expansions
from logger import logger


def check_and_replace():
    typed_text = ""
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name is None:
                continue
            elif event.name == "backspace":
                typed_text = typed_text[:-1]
            elif len(event.name) == 1:
                typed_text += event.name
            elif event.name == "space":
                typed_text += " "
            for shortcut, replacement in load_expansions().items():
                if typed_text.endswith(shortcut):
                    logger.info(f"Replacing: '{shortcut}' -> '{replacement}'")
                    keyboard.write("\b" * len(shortcut))
                    pyperclip.copy(replacement)
                    pyautogui.hotkey("ctrl", "v")
                    typed_text = ""


def start_expander():
    thread = threading.Thread(target=check_and_replace, daemon=True)
    thread.start()
