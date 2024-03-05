from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('CN47N')

sap.option_field('Relat.objeto')