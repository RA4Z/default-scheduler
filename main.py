from sap_functions import SAP

sap = SAP(0)
myGrid = sap.get_my_grid()
print(sap.get_my_grid_count_rows(myGrid))