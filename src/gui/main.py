import wx
from .shortcut_dialogs import AddShortcutDialog
from .utils import prompt_text_dialog


class MainFrame(wx.Frame):
    def __init__(self, replacer):
        super().__init__(None, title="Hypno Type", size=(400, 400))
        self.replacer = replacer
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.list_ctrl = wx.ListCtrl(
            panel,
            style=wx.LC_REPORT | wx.LC_SINGLE_SEL
        )
        self.list_ctrl.InsertColumn(0, "Atalho", width=150)
        self.list_ctrl.InsertColumn(1, "Substituto", width=200)
        self.load_shortcuts_into_list()
        self.list_ctrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
                            self.on_edit_replacement)
        self.list_ctrl.Bind(wx.EVT_KEY_DOWN, self.on_list_key_down)
        self.add_button = wx.Button(panel, label="Adicionar")
        self.add_button.Bind(wx.EVT_BUTTON, self.on_add)
        vbox.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 10)
        vbox.Add(self.add_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        panel.SetSizer(vbox)

    def load_shortcuts_into_list(self):
        self.list_ctrl.DeleteAllItems()
        for item in self.replacer.shortcuts:
            index = self.list_ctrl.InsertItem(
                self.list_ctrl.GetItemCount(),
                item['shortcut']
            )
            self.list_ctrl.SetItem(index, 1, item['replacement'])

    def on_list_key_down(self, event):
        if event.GetKeyCode() == wx.WXK_DELETE:
            self.on_delete_shortcut()
        elif event.GetKeyCode() == wx.WXK_F2:
            self.on_rename_shortcut()
        else:
            event.Skip()

    def on_delete_shortcut(self):
        selected = self.list_ctrl.GetFirstSelected()
        if selected != -1:
            shortcut = self.list_ctrl.GetItemText(selected, 0)
            self.replacer.remove_shortcut(shortcut)
            self.load_shortcuts_into_list()

    def on_rename_shortcut(self):
        selected = self.list_ctrl.GetFirstSelected()
        if selected != -1:
            shortcut = self.list_ctrl.GetItemText(selected, 0)
            new_shortcut = prompt_text_dialog(
                self, "Renomear Atalho", "Atalho", shortcut
            ).strip()
            if new_shortcut and shortcut != new_shortcut:
                if self.replacer.shortcut_exists(new_shortcut):
                    wx.MessageBox(
                        "Erro", "Atalho já existe",
                        wx.OK | wx.ICON_ERROR
                    )
                else:
                    self.replacer.rename_shortcut(shortcut, new_shortcut)
                    self.load_shortcuts_into_list()

    def on_add(self, event):
        dialog = AddShortcutDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            shortcut = dialog.shortcut_input.GetValue().strip()
            replacement = dialog.replacement_input.GetValue().strip()
            if shortcut and replacement:
                enter_after_replace = dialog.enter_after_replace_checkbox.GetValue()
                self.replacer.add_shortcut(
                    shortcut, replacement, enter_after_replace)
                self.load_shortcuts_into_list()
        dialog.Destroy()
        self.list_ctrl.SetFocus()

    def on_edit_replacement(self, event):
        index = event.GetIndex()
        shortcut = self.list_ctrl.GetItemText(index, 1)
        edited_replacement = prompt_text_dialog(
            self, "Editar Substituto", "Substituto", shortcut
        ).strip()
        if edited_replacement and shortcut != edited_replacement:
            shortcut = self.list_ctrl.GetItemText(index, 0)
            self.replacer.edit_replacement(shortcut, edited_replacement)
            self.load_shortcuts_into_list()
        event.Skip()
