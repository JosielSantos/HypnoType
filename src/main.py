from constants import SHORTCUTS_FILE
from gui.main import MainFrame
from replacer import Replacer
import wx


def main():
    replacer = Replacer(SHORTCUTS_FILE)
    replacer.load_shortcuts_file()
    replacer.start()
    app = wx.App(False)
    frame = MainFrame(replacer)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
