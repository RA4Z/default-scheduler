import sys
import os
import datetime
config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(config_dir)
from services.sap_functions import SAP

class Work_SAP():
    def __init__(self, sap:SAP):
        self.path = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Indicadores Automatizados/Indicadores Automatizados (Valmir)/INDICADOR EXPEDIÇÃO'
        self.sap = sap
    
    def LT23(self):
        try:
            current_time = datetime.datetime.now()
            self.sap.select_transaction('LT23')
            self.sap.insert_variant('EXPEDIÇÃO GTA')
            self.sap.write_text_field('Data OT',f'01.01.{current_time.year}')
            self.sap.write_text_field_until('Data OT',f'31.12.{current_time.year}')
            self.sap.run_actual_transaction()
            self.sap.save_file('LT23',self.path,1)
            return True
        except:
            return False
        
    def MB51(self):
        try:
            self.sap.select_transaction('MB51')
            self.sap.clean_all_fields()
            self.sap.insert_variant('WM_PCP_MB51')
            self.sap.run_actual_transaction()
            self.sap.press_button('Lista detalhada')
            self.sap.navigate_into_menu_header('Configurações;Variante de exibição;Selecionar...')
            self.sap.my_grid_select_layout('/WM-PCP_IND.')
            self.sap.save_file('MB51',self.path,1)
            return True
        except:
            return False
        
class Work():
    def __init__(self):
        pass

if __name__ == "__main__":
    work = Work_SAP(SAP(0,False,'PT'))
    work.LT23()
    work.MB51()
    #ZTSD092 - Fazer JOB com variante WEN_PCP_EXP   (Solicitado)
    #LX03 - Fazer JOB com variante /EXPEDICAO_WEN