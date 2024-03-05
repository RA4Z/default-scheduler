import win32com.client
from tkinter import messagebox
import re
import os

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

    def __scroll_through_tabs(self, area, extension, selected_tab):
        children = area.Children
        for child in children:
            if child.Type == "GuiTabStrip": 
                extension = extension + "/tabs" + child.name
                return self.__scroll_through_tabs(self.session.findById(extension), extension, selected_tab)
            if child.Type == "GuiTab": 
                extension = extension + "/tabp" + str(children[selected_tab].name)
                return self.__scroll_through_tabs(self.session.findById(extension), extension, selected_tab)
            if child.Type == "GuiSimpleContainer": 
                extension = extension + "/sub" + child.name
                return self.__scroll_through_tabs(self.session.findById(extension), extension, selected_tab)
            if child.Type == "GuiScrollContainer" and 'tabp' in extension:
                extension = extension + "/ssub" + child.name
                area = self.session.findById(extension)
                return area
        return area
    
    def __scroll_through_fields(self, extension, objective, selected_tab):
        children = self.session.findById(extension).Children
        result = False
        for i in range(len(children)):
            if not result:
                result = self.__generic_conditionals(i, children, objective)
            if result: break
            if not result and children[i].Type == "GuiTabStrip" and not 'ssub' in extension: 
                result = self.__scroll_through_fields(extension + "/tabs" + children[i].name, objective, selected_tab)
            if not result and children[i].Type == "GuiTab" and not 'tabp' in extension: 
                result = self.__scroll_through_fields(extension + "/tabp" + str(children[selected_tab].name), objective, selected_tab)
            if not result and children[i].Type == "GuiSimpleContainer": 
                result = self.__scroll_through_fields(extension + "/sub" + children[i].name, objective, selected_tab)
            if not result and children[i].Type == "GuiScrollContainer":
                result = self.__scroll_through_fields(extension + "/ssub" + children[i].name, objective, selected_tab)
            if not result and children[i].Type == "GuiCustomControl":
                result = self.__scroll_through_fields(extension + "/cntl" + children[i].name, objective, selected_tab)
            if not result and children[i].Type in "GuiShell GuiSplitterShell GuiContainerShell GuiDockShell GuiMenuBar GuiToolbar GuiUserArea GuiTitlebar":
                result = self.__scroll_through_fields(extension + "/" + children[i].name, objective, selected_tab)
        return result

    def __generic_conditionals(self, index, children, objective):
        if objective == 'write_text_field':
            if children(index).Text == self.field_name:
                if self.target_index == 0:
                    try:
                        children(index + 1).Text = self.desired_text
                        return True
                    except Exception as e:
                        print(f'The error {e} has happenned!')
                    return
                else:
                    self.target_index -= 1

        if objective == 'write_text_field_until':
            if children(index).Text == self.field_name:
                if self.target_index == 0:
                    try:
                        children(index + 3).Text = self.desired_text
                        return True
                    except Exception as e:
                        print(f'The error {e} has happenned!')
                    return
                else:
                    self.target_index -= 1

        if objective == 'find_text_field':
            if self.field_name in children(index).Text:
                try:
                    return True
                except Exception as e:
                    print(f'The error {e} has happenned!')
                return
                    
        if objective == 'multiple_selection_field':
            if children(index).Text == self.field_name:
                if self.target_index == 0:
                    try:
                        campo = children(index).name
                        posicaoInicial = campo.find("%") + 1
                        posicaoFinal = campo.find("-", posicaoInicial)
                        campo = campo[posicaoInicial:posicaoFinal] + "-VALU_PUSH"
                        for j in range(index, len(children)):
                            Obj = children[j]
                            if campo in Obj.name:
                                Obj.press()
                                return True
                    except Exception as e:
                        print(f'The error {e} has happenned!')
                    return
                else:
                    self.target_index -= 1
        return False

    def select_transaction(self, transaction):
        self.session.startTransaction(transaction)
        if self.session.activeWindow.name == 'wnd[1]':
            self.session.findById("wnd[1]/usr/ctxtTCNT-PROF_DB").Text = "000000000001"
            self.session.findById("wnd[1]/tbar[0]/btn[0]").press()
        if not self.session.info.transaction == transaction:
            messagebox.showerror(title='Error selecting transaction', message=self.get_footer_message())
            exit()
    
    def select_main_screen(self):
        if not self.session.info.transaction == "SESSION_MANAGER":
            self.session.startTransaction('SESSION_MANAGER')
            if self.session.ActiveWindow.name == "wnd[1]":
                self.session.findById("wnd[1]/tbar[0]/btn[0]").press()

    def clean_all_fields(self, selected_tab = 0):
        self.window = self.__active_window()
        area = self.__scroll_through_tabs(self.session.findById(f"wnd[{self.window}]/usr"), f"wnd[{self.window}]/usr", selected_tab)
        children = area.Children
        for child in children:
            if child.Type == "GuiCTextField":
                try:
                    child.Text = ""
                except Exception as e:
                    print(f'The error {e} has happenned!')

    def insert_variant(self, variant_name):
        try:
            self.session.findById("wnd[0]/tbar[1]/btn[17]").press()
            if self.session.activeWindow.name == 'wnd[1]':
                self.session.findById("wnd[1]/usr/txtV-LOW").Text = variant_name
                self.session.findById("wnd[1]/usr/txtENAME-LOW").Text = ""
                self.session.findById("wnd[1]/tbar[0]/btn[8]").press()
                if self.session.activewindow.name == 'wnd[1]':
                    pass
        except Exception as e:
            print(f'The error {e} has happenned!')

    def change_active_tab(self, selected_tab):
        self.window = self.__active_window()
        area = self.__scroll_through_tabs(self.session.findById(f"wnd[{self.window}]/usr"), f"wnd[{self.window}]/usr", selected_tab)
        try:
            area.Select()
        except Exception as e:
            print(f'The error {e} has happenned!')
        return

    def write_text_field(self, field_name, desired_text, target_index=0, selected_tab=0):
        self.window = self.__active_window()
        self.field_name = field_name
        self.desired_text = desired_text
        self.target_index = target_index
        if selected_tab > 0: self.change_active_tab(selected_tab)
        return self.__scroll_through_fields(f"wnd[{self.window}]/usr", 'write_text_field', selected_tab)

    def write_text_field_until(self, field_name, desired_text, target_index=0, selected_tab=0):
        self.window = self.__active_window()
        self.field_name = field_name
        self.desired_text = desired_text
        self.target_index = target_index
        if selected_tab > 0: self.change_active_tab(selected_tab)
        return self.__scroll_through_fields(f"wnd[{self.window}]/usr", 'write_text_field_until', selected_tab)

    def find_text_field(self, field_name, selected_tab = 0):
        self.window = self.__active_window()
        self.field_name = field_name
        if selected_tab > 0: self.change_active_tab(selected_tab)
        return self.__scroll_through_fields(f"wnd[{self.window}]/usr", 'find_text_field', selected_tab)

    def multiple_selection_field(self, field_name, target_index=0, selected_tab=0):
        self.window = self.__active_window()
        self.field_name = field_name
        self.target_index = target_index
        if selected_tab > 0: self.change_active_tab(selected_tab)
        return self.__scroll_through_fields(f"wnd[{self.window}]/usr", 'multiple_selection_field', selected_tab)

    def multiple_selection_paste_data(self, data):
        try:
            with open('temp_paste.txt', 'w') as arquivo:
                arquivo.write(data)
            self.session.findById("wnd[1]/tbar[0]/btn[23]").press()
            self.session.findById("wnd[2]/usr/ctxtDY_PATH").text = os.getcwd()
            self.session.findById("wnd[2]/usr/ctxtDY_FILENAME").text = "temp_paste.txt"
            self.session.findById("wnd[2]/tbar[0]/btn[0]").press()
            self.session.findById("wnd[1]/tbar[0]/btn[8]").press()
            if os.path.exists('temp_paste.txt'):
                os.remove('temp_paste.txt')
        except Exception as e:
            print(f'The error {e} has happenned!')

    def get_footer_message(self):
        return(self.session.findById("wnd[0]/sbar").Text)
