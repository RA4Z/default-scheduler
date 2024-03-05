from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('MD4C')
sap.clean_all_fields()

sap.write_text_field('Material','1234',selected_tab=1)
print('fim')