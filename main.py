from sap_functions import SAP

sap = SAP(0)
sap.select_transaction('CO02')
sap.write_text_field('Ordem', '1129742056')
sap.press_button('Executar')
sap.press_button('Síntese de componentes')
sap.choose_text_combo('Filtro', 'Filtro manual')
sap.press_button('Procurar')
sap.write_text_field('Condição','Centro')
sap.press_button('Avançar')
sap.press_button('Selecionar marcação')
