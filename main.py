from statements import State
from work_functions import Work_SAP
import progressbar

script = State()
work = Work_SAP(script.sap)

script.app.mainloop()

if script.app.result:
    data = str(script.app.data).split('\n')
    bar = progressbar.ProgressBar(max_value=len(data)-1)

    for i in range(len(data)):
        actual = data[i].strip()
        if actual != '':
            try:
                result = work.co02(actual)
                if result != '':
                    print(f'{actual} => {result}')
                else:
                    print(f'{actual} => Encontrada com sucesso!')
            except Exception as err:
                    print(f'{actual} => {err}')
        bar.update(i)