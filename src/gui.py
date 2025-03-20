import wx
from config import load_expansions, save_expansions


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


class ExpanderApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Hypno Type", size=(400, 400))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, "Atalho", width=150)
        self.list_ctrl.InsertColumn(1, "Expansão", width=200)
        self.load_expansions_into_list()
        self.add_button = wx.Button(panel, label="Adicionar")
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add)
        vbox.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.add_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        panel.SetSizer(vbox)

    def load_expansions_into_list(self):
        self.list_ctrl.DeleteAllItems()
        for shortcut, expansion in load_expansions().items():
            index = self.list_ctrl.InsertItem(
                self.list_ctrl.GetItemCount(), shortcut)
            self.list_ctrl.SetItem(index, 1, expansion)

    def on_add(self, event):
        dialog = AddShortcutDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            shortcut = dialog.shortcut_input.GetValue().strip()
            expansion = dialog.expansion_input.GetValue().strip()
            if shortcut and expansion:
                expansions = load_expansions()
                expansions[shortcut] = expansion
                save_expansions(expansions)
                self.load_expansions_into_list()
        dialog.Destroy()
