import wx
from gui import ExpanderApp
from expander import start_expander


def main():
    start_expander()
    app = wx.App(False)
    frame = ExpanderApp()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
