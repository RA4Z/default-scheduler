from services.sap_functions import SAP

app_name = 'Indicador Expedição'
app_description = ''
app_developer = 'Robert Aron Zimmermann'
app_requester = 'Valmir Junckes'
default_language = 'PT'
login = open('services/sap_login.txt', 'r').readline().strip().split(',')
scheduled_execution = {'scheduled?':True, 'username':login[0], 'password':login[1], 'principal':'100'}
sap_window = 0

class State():
    def __init__(self):
        self.scheduled_execution = scheduled_execution
        self.app_name = app_name
        self.app_developer = app_developer
        self.app_requester = app_requester
        self.default_language = default_language
        self.sap = SAP(sap_window, scheduled_execution, default_language)