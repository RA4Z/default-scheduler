from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('CN47N')
sap.clean_all_fields()