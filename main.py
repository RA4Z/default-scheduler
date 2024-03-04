from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('COHV')
sap.clean_all_fields()

sap.change_active_tab(1)