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
    data = str(script.app.data).split('\n')
    bar = progressbar.ProgressBar(max_value=len(data)-1)
    
    for i in range(len(data)):
        actual = data[i].strip()
        try:
            result = work.co02(actual)
        except Exception as err:
                print(f'{actual} => {err}')
        bar.update(i)

    #SEND AN EXECUTION LOG TO A DATABASE
    try:
        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time = timedelta(seconds=elapsed_time_seconds)
        data_base.post_realtime(script.app_name,str(elapsed_time),i)
    except:
         pass