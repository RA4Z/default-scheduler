from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('ZTPP107')

sap.write_text_field('Centro de produção','1200')
sap.multiple_selection_field('Emissor da ordem')