from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('CN47N')
sap.write_text_field('Elemento PEP', '120-2300872-21')
sap.write_text_field('Layout', '/INI_MONT')
sap.press_button('Executar')
myGrid = sap.get_my_grid()
print(myGrid.getCellValue(0,'LTXA1'))
