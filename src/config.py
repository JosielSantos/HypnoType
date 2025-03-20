import json
import os
import shutil
from constants import EXPANSIONS_FILE
from logger import logger


def load_expansions():
    try:
        with open(EXPANSIONS_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.info(
            "Expansions file not found; Starting with empty expanssions")
        return {}
    except json.JSONDecodeError as e:
        logger.warn(f"Failed to load expansions: Invalid JSON - {e}")
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
