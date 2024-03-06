from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('CJ20N')
sap.press_button('Abrir')
