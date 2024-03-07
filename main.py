from sap_functions import SAP

sap = SAP(1)
#sap.select_transaction('MD04')
#sap.write_text_field('Material','11455340')
#sap.write_text_field('Centro','1200')
#sap.run_actual_transaction()

my_table = sap.get_my_table()
rows = sap.get_my_table_count_visible_rows(my_table)
col_index = sap.get_my_table_column_index(my_table, 'Qtd.disponível')
row_index = sap.get_my_table_row_index(my_table, col_index, '90')
print(row_index)