from config import load_expansions
from constants import APPLICATION_DIRECTORY
from gui import ExpanderApp
from expander import Expander
from logger import logger
import os
import wx


def main():
    expander = Expander(load_expansions())
    expander.start()
    app = wx.App(False)
    frame = ExpanderApp(expander)
    frame.Show()
    app.MainLoop()
    logger.debug('Application started')


if __name__ == "__main__":
    if not os.path.exists(APPLICATION_DIRECTORY):
        os.makedirs(APPLICATION_DIRECTORY)
    main()
    logger.debug('Application terminated')
