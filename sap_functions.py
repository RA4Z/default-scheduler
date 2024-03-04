import win32com.client
from tkinter import messagebox
import re

#module SAP Functions, development started in 2024/03/01
class SAP():
    def __init__(self, window: int):
        sapguiauto = win32com.client.GetObject('SAPGUI')
        application = sapguiauto.GetScriptingEngine
        connection = application.Children(0)
        self.session = connection.Children(window)
        self.window = self.__active_window()

    def __active_window(self):
        regex = re.compile('[0-9]')
        matches = regex.findall(self.session.ActiveWindow.name)
        for match in matches:
            return match

    def __scroll_through_tab(self, area, extensao, selected_tab):
        children = area.Children
        for child in children:
            if child.Type == "GuiTabStrip": 
                extensao = extensao + "/tabs" + child.name
                return self.__scroll_through_tab(self.session.findById(extensao), extensao, selected_tab)
            if child.Type == "GuiTab": 
                extensao = extensao + "/tabp" + str(children[selected_tab].name)
                return self.__scroll_through_tab(self.session.findById(extensao), extensao, selected_tab)
            if child.Type == "GuiSimpleContainer": 
                extensao = extensao + "/sub" + child.name
                return self.__scroll_through_tab(self.session.findById(extensao), extensao, selected_tab)
            if child.Type == "GuiScrollContainer" and 'tabp' in extensao:
                extensao = extensao + "/ssub" + child.name
                area = self.session.findById(extensao)
                return area
        return area

    def select_transaction(self, transaction):
        self.session.startTransaction(transaction)
        if self.session.activeWindow.name == 'wnd[1]':
            self.session.findById("wnd[1]/usr/ctxtTCNT-PROF_DB").Text = "000000000001"
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        if not self.session.info.transaction == transaction:
            messagebox.showerror(title='Erro ao Selecionar Transação', message=self.get_footer_message())
            exit()
    
    def select_main_screen(self):
        if not self.session.info.transaction == "SESSION_MANAGER":
            self.session.startTransaction('SESSION_MANAGER')
            if self.session.ActiveWindow.name == "wnd[1]":
                self.session.findById("wnd[1]/tbar[0]/btn[0]").press()

    def clean_all_fields(self, selected_tab = 0):
        self.window = self.__active_window()
        area = self.__scroll_through_tab(self.session.findById(f"wnd[{self.window}]/usr"), f"wnd[{self.window}]/usr", selected_tab)
        children = area.Children
        for child in children:
            if child.Type == "GuiCTextField":
                try:
                    child.Text = ""
                except:
                    pass

    def get_footer_message(self):
        return(self.session.findById("wnd[0]/sbar").Text)
