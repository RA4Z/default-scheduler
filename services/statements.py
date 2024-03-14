from services.sap_functions import SAP
from interface.frm_main import Application

app_name = 'Python Default Script'
app_description = 'Graphical interface model developed in Tkinter by Robert Aron Zimmermann, an interface was developed to be used as a basis in the development of other automations that are interactive with SAP, the entire algorithm was developed in Python with the intention of facilitating interaction between Developer/ SAP, thus developing high quality automation in a short period of time with several error treatments. Doubts or Suggestions contact Robert Aron Zimmermann robertn@weg.net'
app_developer = 'Robert Aron Zimmermann'
app_requester = 'Robert Aron Zimmermann'
app_columns = ['Column 1','Column 2','Column 3']
scheduled_execution = {'scheduled?':False, 'username':'robertn', 'password':'4@@2oitonove22', 'principal':'100'}
sap_window = 0

class State():
    def __init__(self):
        self.app_columns = app_columns
        self.scheduled_execution = scheduled_execution
        self.app_name = app_name
        self.sap = SAP(sap_window, scheduled_execution)
        if not self.scheduled_execution['scheduled?']: self.app = Application(app_name,app_description,app_developer,app_requester,app_columns)