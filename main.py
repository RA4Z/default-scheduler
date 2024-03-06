from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('MD04')
sap.run_actual_transaction()

my_table = sap.get_my_table()
children = my_table.Children
print(children.Count)