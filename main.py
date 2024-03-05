from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('ZTPP107')

sap.write_text_field('Centro de produção','1200')
sap.multiple_selection_field('Centro de produção')
sap.multiple_selection_paste_data('1201\n1220')