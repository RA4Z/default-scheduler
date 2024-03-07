from statements import State

script = State()
script.app.mainloop()

if script.app.result: 
    print(script.app.data)
    script.sap.select_transaction('MD4C')