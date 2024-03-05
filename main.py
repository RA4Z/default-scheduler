from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('COHV')
sap.insert_variant('/NADA')