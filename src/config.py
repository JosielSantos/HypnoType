import json
import os
import shutil

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".hypno-type")
EXPANSIONS_FILE = os.path.join(CONFIG_DIR, "expansions.json")

if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)


def load_expansions():
    try:
        with open(EXPANSIONS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_expansions(expansions):
    if os.path.exists(EXPANSIONS_FILE):
        shutil.copy(EXPANSIONS_FILE, EXPANSIONS_FILE + ".bak")
    with open(EXPANSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(expansions, f, indent=4)
