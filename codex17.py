import PySimpleGUI as sg


feet_label = sg.Text("Enter feet: ")
input_feet = sg.InputText(tooltip="Enter feet", key="feet")

inches_label = sg.Text("Enter inches: ")
input_inches = sg.InputText(tooltip="Enter inches", key="inches")

convert_btn = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, input_feet],
                           [inches_label, input_inches],
                           [convert_btn, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            result = feet*0.3048 +inches*0.0254
            print(result)
            window["output"].update(value=f"{result} m", text_color="white")

        case sg.WIN_CLOSED:
            break


window.close()