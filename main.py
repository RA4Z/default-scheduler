from datetime import timedelta
import time
from statements import State
from work_functions import Work_SAP
from config.firebase import Firebase
import progressbar

script = State()
work = Work_SAP(script.sap)
data_base = Firebase()

script.app.mainloop()

if script.app.result:
    start_time = time.time()
    colunas = {}

    for item in script.app.data:
        colunas[item['column_name']] = str(item['text']).split('\n')[:-1]
        while len(colunas[item['column_name']]) < len(colunas[script.app.data[0]['column_name']]):
            colunas[item['column_name']].append('')
            
    bar = progressbar.ProgressBar(max_value=len(colunas[script.app.data[0]['column_name']])-1)

    # - - - - - - - - - - - - - - - - - - - WRITE YOUR CODE THERE - - - - - - - - - - - - - - - - - - - #
    for i in range(len(colunas[script.app.data[0]['column_name']])):
        bar.update(i)
        print(f"Value Column 1 = {colunas['Column 1'][i]}; Value Column 2 = {colunas['Column 2'][i]}; Value Column 3 = {colunas['Column 3'][i]}")
    # - - - - - - - - - - - - - - - - - - - WRITE YOUR CODE THERE - - - - - - - - - - - - - - - - - - - #


    #SEND AN EXECUTION LOG TO A DATABASE
    try:
        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time = timedelta(seconds=elapsed_time_seconds)
        data_base.post_realtime(script.app_name,str(elapsed_time),i)
    except:
         pass