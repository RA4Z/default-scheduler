from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('COOIS')

sap.press_button('Chamar variante...')
sap.press_button('Executar')