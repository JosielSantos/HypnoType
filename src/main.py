from constants import APPLICATION_DIRECTORY
from gui import ExpanderApp
from expander import start_expander
from logger import logger
import os
import wx


def main():
    start_expander()
    app = wx.App(False)
    frame = ExpanderApp()
    frame.Show()
    app.MainLoop()
    logger.debug('Application started')


if __name__ == "__main__":
    if not os.path.exists(APPLICATION_DIRECTORY):
        os.makedirs(APPLICATION_DIRECTORY)
    main()
    logger.debug('Application terminated')
