import wx


class AddShortcutDialog(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Adicionar Atalho", size=(300, 200))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        wx.StaticText(panel, label="Atalho:")
        self.shortcut_input = wx.TextCtrl(panel)
        vbox.Add(self.shortcut_input, 0, wx.EXPAND | wx.ALL, 5)
        wx.StaticText(panel, label="Expansão:")
        self.expansion_input = wx.TextCtrl(panel)
        vbox.Add(self.expansion_input, 0, wx.EXPAND | wx.ALL, 5)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.ok_button = wx.Button(panel, label="OK")
        self.cancel_button = wx.Button(panel, label="Cancelar")
        hbox.Add(self.ok_button, 1, wx.EXPAND | wx.ALL, 5)
        hbox.Add(self.cancel_button, 1, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox, 0, wx.ALIGN_CENTER)
        self.ok_button.Bind(wx.EVT_BUTTON, self.on_ok)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        panel.SetSizer(vbox)

    def on_ok(self, event):
        self.EndModal(wx.ID_OK)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)
