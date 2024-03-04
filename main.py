from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('ZTPP107')
sap.clean_all_fields()