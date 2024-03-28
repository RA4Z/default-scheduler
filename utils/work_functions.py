import sys
import os
config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(config_dir)
from services.sap_functions import SAP

class Work_SAP():
    def __init__(self, sap:SAP):
        self.sap = sap
        
class Work():
    def __init__(self):
        pass