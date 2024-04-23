from services.language_dict import Language
from services.statements import State
from utils.work_functions import Work_SAP
from services.excel import ExcelHandler
from services.outlook import Outlook
from web.browser_selenium import SeleniumBrouser

def main():
    script = State()
    work = Work_SAP(script.sap)
    web = SeleniumBrouser()
    sheet_excel = ExcelHandler('')
    mail_outlook = Outlook()
    language = Language(script.default_language)
    i = 0
    atualizadas = ''

    if work.LT23(): 
        i += 1
        atualizadas = f'{atualizadas}LT23; '

    if work.MB51(): 
        i += 1
        atualizadas = f'{atualizadas}MB51; '

    return f'Foram atualizados {i}/2 bases de dados sendo elas: {atualizadas}'

if __name__ == "__main__":
    print(main())