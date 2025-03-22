import json
import keyboard
import pyperclip
import pyautogui
import os
import shutil
import threading
import winsound
from clipboard import ClipboardBackup
from constants import SOUNDS_DIRECTORY
from logger import logger


class Replacer:
    def __init__(self, shortcuts_file):
        self.shortcuts_file = shortcuts_file
        self.shortcuts = []

    def load_shortcuts_file(self):
        try:
            with open(self.shortcuts_file, encoding="utf-8") as f:
                self.shortcuts = json.load(f)
        except FileNotFoundError:
            logger.info(
                "shortcuts file not found; Continuing with empty list"
            )
            self.shortcuts = []
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to load shortcuts: Invalid JSON - {e}")
            self.shortcuts = []

    def start(self):
        thread = threading.Thread(
            target=self.monitor_keyboard_and_replace_text,
            daemon=True
        )
        thread.start()

    def monitor_keyboard_and_replace_text(self):
        typed_text = ""
        while True:
            if not self.shortcuts:
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
                for item in self.shortcuts:
                    if typed_text.endswith(item['shortcut']):
                        self.replace_shortcut(
                            item['shortcut'],
                            item['replacement'],
                            item['enter_after_replace']
                        )
                        typed_text = ""

    def replace_shortcut(self, shortcut, replacement, enter_after_replace):
        clipboard_backup = ClipboardBackup()
        clipboard_backup.save()
        logger.info(
            f"Replacing: '{shortcut}' -> '{replacement}'"
        )
        keyboard.write("\b" * len(shortcut))
        pyperclip.copy(replacement)
        pyautogui.hotkey("ctrl", "v")
        clipboard_backup.restore()
        if enter_after_replace:
            keyboard.send('enter')
        winsound.PlaySound(
            SOUNDS_DIRECTORY + "/text_expanded.wav",
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    def add_shortcut(self, shortcut, replacement, enter_after_replace):
        self.shortcuts.append({
            'shortcut': shortcut,
            'replacement': replacement,
            'enter_after_replace': enter_after_replace,
        })
        self.save_shortcuts_file()

    def edit_replacement(self, shortcut, new_replacement):
        for item in self.shortcuts:
            if item.get("shortcut") == shortcut:
                item["replacement"] = new_replacement
                self.save_shortcuts_file()
                break

    def remove_shortcut(self, shortcut):
        self.shortcuts = [
            item for item in self.shortcuts if item.get("shortcut") != shortcut
        ]
        self.save_shortcuts_file()

    def rename_shortcut(self, old_shortcut, new_shortcut):
        for item in self.shortcuts:
            if item.get("shortcut") == old_shortcut:
                item["shortcut"] = new_shortcut
                self.save_shortcuts_file()
                break

    def shortcut_exists(self, shortcut):
        return any(item.get("shortcut") == shortcut for item in self.shortcuts)

    def save_shortcuts_file(self):
        self.backup_shortcuts_file()
        try:
            with open(self.shortcuts_file, "w", encoding="utf-8") as f:
                json.dump(self.shortcuts, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save shortcuts: {e}")
            raise e

    def backup_shortcuts_file(self):
        if os.path.exists(self.shortcuts_file):
            try:
                shutil.copy(
                    self.shortcuts_file,
                    self.shortcuts_file + ".bak"
                )
            except Exception as e:
                logger.warning(f"Failed to create backup of shortcuts: {e}")
