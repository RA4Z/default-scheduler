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
                work.cn47n(data.strip()) #PUT YOUR CODE THERE
            except Exception as err:
                print(err)