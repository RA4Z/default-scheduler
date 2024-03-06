from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('MD04')
sap.run_actual_transaction()
sap.press_button('Planejamento individual interativo')
