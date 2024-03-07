from sap_functions import SAP

sap = SAP(1)
#sap.select_transaction('MD04')
#sap.write_text_field('Material','11455340')
#sap.write_text_field('Centro','1200')
#sap.run_actual_transaction()

my_table = sap.get_my_table()
rows = sap.get_my_table_count_visible_rows(my_table)
for i in range(rows):
    print(f'MRP = {sap.my_table_get_cell_value(my_table, i, 2)} Entrada = {sap.my_table_get_cell_value(my_table, i, 4)}')