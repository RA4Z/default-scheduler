import win32com.client
from tkinter import messagebox
#module SAP Functions, development started in 2024/03/01
class SAP():
    def __init__(self, window: int):
        sapguiauto = win32com.client.GetObject('SAPGUI')
        application = sapguiauto.GetScriptingEngine
        connection = application.Children(0)
        self.session = connection.Children(window)
    
    def select_transaction(self, transaction):
        self.session.startTransaction(transaction)
        if self.session.activeWindow.name == 'wnd[1]':
            self.session.findById("wnd[1]/usr/ctxtTCNT-PROF_DB").Text = "000000000001"
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        if not self.session.info.transaction == transaction:
            messagebox.showerror(title='Erro ao Selecionar Transação', message=self.get_footer_message())
            exit()
    
    def get_footer_message(self):
        return(self.session.findById("wnd[0]/sbar").Text)
