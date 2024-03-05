from sap_functions import SAP

sap = SAP(1)
sap.select_transaction('CN47N')
sap.write_text_field('Elemento PEP', '120-2300872-21')
sap.write_text_field('Layout', '/INI_MONT')
sap.press_button('Executar')
sap.view_in_list_form()
sap.save_file('teste','Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/Central/00-Planilha_Padrão')
