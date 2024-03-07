from statements import State

script = State()
script.app.mainloop()

if script.app.result: 
    script.sap.select_transaction('MD4C')