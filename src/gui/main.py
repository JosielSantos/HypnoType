import wx
from .expansion_dialogs import AddShortcutDialog
from .utils import prompt_text_dialog


class MainFrame(wx.Frame):
    def __init__(self, expander):
        super().__init__(None, title="Hypno Type", size=(400, 400))
        self.expander = expander
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.list_ctrl = wx.ListCtrl(
            panel,
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL
        )
        self.list_ctrl.InsertColumn(0, "Atalho", width=150)
        self.list_ctrl.InsertColumn(1, "Expansão", width=200)
        self.load_expansions_into_list()
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_edit_expansion)
        self.list_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_list_key_down)
        self.add_button = wx.Button(panel, label="Adicionar")
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add)
        vbox.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.add_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        panel.SetSizer(vbox)

    def load_expansions_into_list(self):
        self.list_ctrl.DeleteAllItems()
        for shortcut, expansion in self.expander.expansions.items():
            index = self.list_ctrl.InsertItem(
                self.list_ctrl.GetItemCount(),
                shortcut
            )
            self.list_ctrl.SetItem(index, 1, expansion)

    def on_list_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.on_delete_expansion()
        elif event.GetKeyCode() == wx.WXK_F2:
            self.on_rename_shortcut()
        else:
            event.Skip()

    def on_delete_expansion(self):
        selected = self.list_ctrl.GetFirstSelected()
        if selected != -1:
            shortcut = self.list_ctrl.GetItemText(selected, 0)
            self.expander.remove_expansion(shortcut)
            self.load_expansions_into_list()

    def on_rename_shortcut(self):
        selected = self.list_ctrl.GetFirstSelected()
        if selected != -1:
            shortcut = self.list_ctrl.GetItemText(selected, 0)
            new_shortcut = prompt_text_dialog(
                self, "Renomear Atalho", "Atalho", shortcut).strip()
            if new_shortcut and shortcut != new_shortcut:
                if self.expander.shortcut_exists(new_shortcut):
                    wx.MessageBox(
                        "Erro", "Atalho já existe",
                        wx.OK | wx.ICON_ERROR
                    )
                else:
                    self.expander.rename_shortcut(shortcut, new_shortcut)
                    self.load_expansions_into_list()

    def on_add(self, event):
        dialog = AddShortcutDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            shortcut = dialog.shortcut_input.GetValue().strip()
            expansion = dialog.expansion_input.GetValue().strip()
            if shortcut and expansion:
                self.expander.add_or_replace_expansion(shortcut, expansion)
                self.load_expansions_into_list()
        dialog.Destroy()
        self.list_ctrl.SetFocus()
        event.Skip()

    def on_edit_expansion(self, event):
        index = event.GetIndex()
        expansion = self.list_ctrl.GetItemText(index, 1)
        edited_expansion = prompt_text_dialog(
            self, "Editar expansão", "Expansão", expansion
        ).strip()
        if edited_expansion and expansion != edited_expansion:
            shortcut = self.list_ctrl.GetItemText(index, 0)
            self.expander.add_or_replace_expansion(shortcut, edited_expansion)
            self.load_expansions_into_list()
        event.Skip()
