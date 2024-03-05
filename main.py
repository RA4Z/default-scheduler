from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('COHV')
sap.clean_all_fields()

sap.multiple_selection_field('Centro')