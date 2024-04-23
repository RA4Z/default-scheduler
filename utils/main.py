import time

import sys
import os
config_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(config_dir)

from services.language_dict import Language
from services.statements import State
from utils.work_functions import Work_SAP
from services.excel import ExcelHandler
from services.outlook import Outlook
from web.browser_selenium import SeleniumBrouser

script = State()
work = Work_SAP(script.sap)
web = SeleniumBrouser()
sheet_excel = ExcelHandler('')
mail_outlook = Outlook()
language = Language(script.default_language)
i = 0

time.sleep(0.571)

print('complete')