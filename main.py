from sap_functions import SAP

sap = SAP(1)
sap.select_transaction('MD04')
sap.write_text_field('Material','11455340')
sap.write_text_field('Centro','1200')
sap.run_actual_transaction()

my_table = sap.get_my_table()
rows = my_table.VisibleRowCount
print(f'Visible Rows: {my_table.VisibleRowCount}, Total Rows: {my_table.RowCount}')
total_loop = my_table.RowCount
loop_index = 0
while total_loop > rows:
    if loop_index > 0:
        total_loop -= rows
        sap.session.findById("wnd[0]").sendVKey(82)
        my_table = sap.get_my_table()
    for i in range(rows): 
        if i == 0 and total_loop < my_table.RowCount: i += 1
        print(f'Data = {sap.my_table_get_cell_value(my_table,i,1)}')
        loop_index += 1
print(f'Total Loop = {my_table.RowCount - (rows - 1)}; Loop Index = {loop_index}')