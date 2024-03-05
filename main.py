from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('COHV')
sap.clean_all_fields()

sap.write_text_field('Material','1234')
sap.write_text_field_until('Material','4321')
print(sap.find_text_field('Lista'))