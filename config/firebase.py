import requests
import json
import getpass
import datetime

class Firebase():
    def __init__(self):
        self.link = 'https://default-python-default-rtdb.firebaseio.com/'

    def post_realtime(self, script_name:str, duration:str, quantity:int):
        data = {'nomeUser':getpass.getuser().upper(),'nomeAlgoritmo':script_name,'duracao':duration,'horaExec':str(datetime.datetime.now()),'quantidade':quantity}
        self.requisition = requests.post(f'{self.link}/Algoritmos/.json', data=json.dumps(data), verify=False)
