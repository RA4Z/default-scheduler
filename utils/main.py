from datetime import timedelta
from tkinter import messagebox
import time

import sys
import os
config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(config_dir)

from services.language_dict import Language
from services.statements import State
from utils.work_functions import Work_SAP
from config.firebase import Firebase
from services.excel import ExcelHandler
from services.outlook import Outlook
import progressbar

script = State()
work = Work_SAP(script.sap)
sheet_excel = ExcelHandler('')
mail_outlook = Outlook()
data_base = Firebase()
language = Language(script.default_language)
i = 0

if not script.scheduled_execution['scheduled?']: script.app.mainloop()

if script.app.result or script.scheduled_execution['scheduled?']:
    start_time = time.time()

    if not script.scheduled_execution['scheduled?']:
        colunas = {}
        for item in script.app.data:
            colunas[item['column_name']] = str(item['text']).split('\n')[:-1]
            while len(colunas[item['column_name']]) < len(colunas[script.app.data[0]['column_name']]):
                colunas[item['column_name']].append('')
                
        bar = progressbar.ProgressBar(max_value=len(colunas[script.app.data[0]['column_name']])-1)

        # - - - - - - - - - - - - - - - - - - - WRITE YOUR UNSCHEDULED CODE THERE - - - - - - - - - - - - - - - - - - - #
        for i in range(len(colunas[script.app.data[0]['column_name']])):
            bar.update(i)
            time.sleep(3)
        # - - - - - - - - - - - - - - - - - - - WRITE YOUR UNSCHEDULED CODE THERE - - - - - - - - - - - - - - - - - - - #
            
    else:
        # - - - - - - - - - - - - - - - - - - - WRITE YOUR SCHEDULED CODE THERE - - - - - - - - - - - - - - - - - - - #
        time.sleep(5.571)
        # - - - - - - - - - - - - - - - - - - - WRITE YOUR SCHEDULED CODE THERE - - - - - - - - - - - - - - - - - - - #


    #SEND AN EXECUTION LOG TO A DATABASE
    try:
        end_time = time.time()
        elapsed_time_seconds = end_time - start_time
        elapsed_time = timedelta(seconds=elapsed_time_seconds)
        data_base.post_realtime(script.app_name,str(elapsed_time),i + 1)
    except:
         pass
    
    if not script.scheduled_execution['scheduled?']: messagebox.showinfo(language.search('end_execution_title'),language.search('end_execution_body'))