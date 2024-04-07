import PySimpleGUI as sg
# import time

# All the stuff inside your window.
layout = [
    [sg.Text("Enter two numbers:")],
    [sg.InputText(key="-A-")],
    [sg.InputText(key="-B-")],
    [sg.Text(key="-RESULT-")],
    [sg.Button('Multiply!'), sg.Button('Cancel')]
]

# Create the Window
window = sg.Window('Calculator :D', layout)


# Event loop to process "events" and get the "values" of the inputs
while True:

    ### Boilerplate
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    window["-A-"].update("")
    window["-B-"].update("")

    ### Do something useful
    # if values["-A-"] == values["-B-"] == "":
    if not any(values):
        print("No values entered :|")
        continue

    if (not values["-A-"].isnumeric()) or (not values["-B-"].isnumeric()):
    # if any(i for i in values if (not i.isnumeric())):
        print("Please enter numeric values only! :o")
        continue

    result = int(values["-A-"]) * int(values["-B-"])
    window["-RESULT-"].update(result)


window.close()
