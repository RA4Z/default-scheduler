from sap_functions import SAP

class Work_SAP():
    def __init__(self, sap:SAP):
        self.sap = sap
    
    def cn47n(self, data:str):
        self.sap.select_transaction('CN47N')
        self.sap.write_text_field('Elemento PEP',data)
        self.sap.write_text_field('Layout','/INI_MONT')
        self.sap.run_actual_transaction()
        self.sap.view_in_list_form()

    def co02(self,data:str):
        self.sap.select_transaction('CO02')
        self.sap.write_text_field('Ordem',data)
        self.sap.run_actual_transaction()
        return self.sap.get_footer_message()

class Work():
    def __init__(self):
        pass