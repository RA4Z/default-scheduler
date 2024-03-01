import win32com.client
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

