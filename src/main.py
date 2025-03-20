from constants import APPLICATION_DIRECTORY, EXPANSIONS_FILE
from gui.main import MainFrame
from expander import Expander
from logger import logger
import os
import wx


def main():
    expander = Expander(EXPANSIONS_FILE)
    expander.load_expansions_file()
    expander.start()
    app = wx.App(False)
    frame = MainFrame(expander)
    frame.Show()
    app.MainLoop()
    logger.debug('Application started')


if __name__ == "__main__":
    if not os.path.exists(APPLICATION_DIRECTORY):
        os.makedirs(APPLICATION_DIRECTORY)
    main()
    logger.debug('Application terminated')
