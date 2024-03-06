from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('MD04')
sap.run_actual_transaction()

my_table = sap.get_my_table()
rows = sap.get_my_table_count_rows(my_table)
col = sap.get_my_table_column_index(my_table, 'Depósito')

print(col)