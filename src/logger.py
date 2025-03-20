import logging
import os
from config import APPLICATION_DIRECTORY

LOG_FILE = os.path.join(APPLICATION_DIRECTORY, "hypno-type.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s -> %(asctime)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Hypno Type")
