from gui import ExpanderApp
from expander import start_expander
from logger import logger
import wx


def main():
    start_expander()
    app = wx.App(False)
    frame = ExpanderApp()
    frame.Show()
    app.MainLoop()
    logger.debug('Application started')


if __name__ == "__main__":
    main()
    logger.debug('Application terminated')
