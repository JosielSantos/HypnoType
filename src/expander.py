import json
import keyboard
import pyperclip
import pyautogui
import os
import shutil
import threading
from logger import logger


class Expander:
    def __init__(self, expansions_file):
        self.expansions_file = expansions_file
        self.expansions = {}

    def load_expansions_file(self):
        try:
            with open(self.expansions_file, encoding="utf-8") as f:
                self.expansions = json.load(f)
        except FileNotFoundError:
            logger.info(
                "Expansions file not found; Starting with empty expanssions"
            )
            self.expansions = {}
        except json.JSONDecodeError as e:
            logger.warn(f"Failed to load expansions: Invalid JSON - {e}")
            self.expansions = {}

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

    def add_or_edit_expansion(self, shortcut, expansion):
        self.expansions[shortcut] = expansion
        self.save_expansions_file()

    def remove_expansion(self, shortcut):
        if shortcut in self.expansions:
            del self.expansions[shortcut]
            self.save_expansions_file()

    def save_expansions_file(self):
        self.backup_expansions_file()
        try:
            with open(self.expansions_file, "w", encoding="utf-8") as f:
                json.dump(self.expansions, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save expansions: {e}")
            raise e

    def backup_expansions_file(self):
        if os.path.exists(self.expansions_file):
            try:
                shutil.copy(
                    self.expansions_file,
                    self.expansions_file + ".bak"
                )
            except Exception as e:
                logger.warn(f"Failed to create backup of expansions: {e}")
