from statements import State
from work_functions import Work_SAP

script = State()
work = Work_SAP(script.sap)

script.app.mainloop()

if script.app.result:
    all_data = str(script.app.data).split('\n')

    for data in all_data:
        if data.strip() != '':
            try:
                result = work.co02(data.strip()) #PUT YOUR CODE THERE
                if result != '':
                    print(f'{data.strip()} => {result}')
                else:
                    print(f'{data.strip()} => Encontrada com sucesso!')
            except Exception as err:
                    print(f'{data.strip()} => {err}')