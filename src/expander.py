import keyboard
import pyperclip
import pyautogui
import threading
from logger import logger


class Expander:
    def __init__(self, expansions):
        self.expansions = expansions

    def start(self):
        thread = threading.Thread(
            target=self.monitor_keyboard_and_expand_text,
            daemon=True
        )
        thread.start()

    def monitor_keyboard_and_expand_text(self):
        typed_text = ""
        while True:
            if not self.expansions:
                continue
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
                for shortcut, replacement in self.expansions.items():
                    if typed_text.endswith(shortcut):
                        logger.info(
                            f"Replacing: '{shortcut}' -> '{replacement}'")
                        keyboard.write("\b" * len(shortcut))
                        pyperclip.copy(replacement)
                        pyautogui.hotkey("ctrl", "v")
                        typed_text = ""
