import requests
import json
import getpass
import datetime
import urllib3

urllib3.disable_warnings()
class Firebase():
    def __init__(self):
        self.link = 'https://default-python-default-rtdb.firebaseio.com/'

    # CREATE A LOG OF EXECUTION IN REALTIME DATABASE
    def post_realtime(self, script_name:str, duration:str, quantity:int):
        data = {'duracao':duration,'horaExec':str(datetime.datetime.now()),'quantidade':quantity}
        self.requisition = requests.post(f'{self.link}/Algoritmos/{script_name}/{getpass.getuser().upper()}/.json', data=json.dumps(data), verify=False)

    # MAKE ALTERATIONS IN A SPECIFIC LOG
    def patch_realtime(self,id:str,username:str,script_name:str,hour_exec:str,duration:str,quantity:int):
        data = {'duracao':duration,'horaExec':hour_exec,'quantidade':quantity}
        self.requisition = requests.patch(f'{self.link}/Algoritmos/{script_name}/{username}/{id}/.json', data=json.dumps(data), verify=False)

    # GET ALL THE LOGS INSIDE THE DATABASE
    def get_realtime(self, script_name:str):
        self.requisition = requests.get(f'{self.link}/Algoritmos/{script_name}/{getpass.getuser().upper()}/.json', verify=False).json()
        return self.requisition
