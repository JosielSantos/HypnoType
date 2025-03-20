import json
import os
import shutil
from logger import logger


APPLICATION_DIRECTORY = os.path.join(os.path.expanduser("~"), ".hypno-type")
EXPANSIONS_FILE = os.path.join(APPLICATION_DIRECTORY, "expansions.json")


if not os.path.exists(APPLICATION_DIRECTORY):
    os.makedirs(APPLICATION_DIRECTORY)


def load_expansions():
    try:
        with open(EXPANSIONS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_expansions(expansions):
    if os.path.exists(EXPANSIONS_FILE):
        try:
            shutil.copy(EXPANSIONS_FILE, EXPANSIONS_FILE + ".bak")
        except Exception as e:
            logger.warn(f"Failed to create backup of expansions: {e}")
    try:
        with open(EXPANSIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(expansions, f, indent=4)
    except Exception as e:
        logger.error(f"Failed to save expansions: {e}")
        raise e
