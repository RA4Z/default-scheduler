from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('CN47N')
print(sap.find_text_field('Layout'))