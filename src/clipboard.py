import pywintypes
import win32api
import win32clipboard
from logger import logger


class ClipboardBackup:
    def __init__(self):
        self._backup = None

    def save(self):
        self._backup = {}
        win32clipboard.OpenClipboard()
        try:
            fmt = 0
            while True:
                fmt = win32clipboard.EnumClipboardFormats(fmt)
                if fmt == 0:
                    last_error = win32api.GetLastError()
                    if last_error == 0:
                        break
                    else:
                        logger.warn(f"Error when enumerating clipboard formats: {last_error}")
                try:
                    data = win32clipboard.GetClipboardData(fmt)
                    self._backup[fmt] = data
                except (TypeError, pywintypes.error) as e:
                    self._backup[fmt] = None
                    logger.warn(f"Failed when getting clipboard data with format {fmt}: {e}")
        finally:
            win32clipboard.CloseClipboard()

    def restore(self):
        if self._backup is None:
            return
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            for fmt, data in self._backup.items():
                if data is not None:
                    try:
                        win32clipboard.SetClipboardData(fmt, data)
                    except Exception as e:
                        logger.warn(f"Failed when restoring clipboard data with format {fmt}: {e}")
        finally:
            win32clipboard.CloseClipboard()
