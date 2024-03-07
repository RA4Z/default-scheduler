from statements import State

script = State()
script.app.mainloop()

if script.app.result:
    all_data = str(script.app.data).split('\n')

    for data in all_data:
        if data.strip() != '':
            pass    #PUT YOUR CODE THERE