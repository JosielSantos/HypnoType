import wx


def prompt_text_dialog(parent, dialog_title, edit_label, value=''):
    dialog = wx.TextEntryDialog(
        parent,
        caption=dialog_title,
        message=edit_label,
        value=str(value)
    )
    dialog.ShowModal()
    result = dialog.GetValue()
    dialog.Destroy()
    return result
