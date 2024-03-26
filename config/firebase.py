import requests
import json
import getpass
import datetime
import urllib3
from random import randint

urllib3.disable_warnings()
class Firebase():
    def __init__(self):
        self.link = 'https://default-python-default-rtdb.firebaseio.com/'

    # CREATE A LOG OF EXECUTION IN REALTIME DATABASE
    def post_realtime(self, script_name:str, duration:str, quantity:int):
        data = {'duracao':duration,'horaExec':str(datetime.datetime.now()),'quantidade':quantity}
        self.requisition = requests.post(f'{self.link}/Algoritmos/{script_name}/{getpass.getuser().upper()}/.json', data=json.dumps(data), verify=False)

    # CREATE A LOG OF EXECUTION IN REALTIME DATABASE
    def post_error(self, script_name:str, message:str):
        data = {'horaExec':str(datetime.datetime.now()),'mensagem':message}
        self.requisition = requests.post(f'{self.link}/Erros/{script_name}/{getpass.getuser().upper()}/.json', data=json.dumps(data), verify=False)

    # MAKE ALTERATIONS IN A SPECIFIC LOG
    def patch_realtime(self,id:str,username:str,script_name:str,hour_exec:str,duration:str,quantity:int):
        data = {'duracao':duration,'horaExec':hour_exec,'quantidade':quantity}
        self.requisition = requests.patch(f'{self.link}/Algoritmos/{script_name}/{username}/{id}/.json', data=json.dumps(data), verify=False)

    # GET ALL THE LOGS INSIDE THE DATABASE
    def get_realtime(self, script_name:str):
        self.requisition = requests.get(f'{self.link}/Algoritmos/{script_name}/{getpass.getuser().upper()}/.json', verify=False).json()
        return self.requisition

    # GET QUICK TIPS OR NEWS FROM THE DATABASE
    def get_tips_or_news(self):
        self.requisition = requests.get(f'{self.link}/Noticias/.json', verify=False).json()
        return self.requisition[randint(0,len(self.requisition)-1)]
    
    # GET ALL THE LOGS INSIDE THE DATABASE
    def get_mid_time(self, script_name:str, desired_total:int):
        record = requests.get(f'{self.link}/Algoritmos/{script_name}/.json', verify=False).json()
        if record != None:
            quantity = 0
            total_seconds = 0
            for user in record:
                for id in record[user]:
                    time = datetime.datetime.strptime(record[user][id]['duracao'],"%H:%M:%S.%f").time()
                    quantity = quantity + record[user][id]['quantidade']
                    total_seconds = total_seconds + (time.hour * 3600) + (time.minute * 60) + time.second + (time.microsecond / 1000000)

            result_seconds = (total_seconds / quantity) * desired_total
            resultado_timedelta = datetime.timedelta(seconds=result_seconds)
            resultado_datetime = datetime.datetime.min + resultado_timedelta
            media_unit = resultado_datetime.time()
            self.requisition = str(media_unit).split('.')[0]
            return self.requisition
        else:
            return None