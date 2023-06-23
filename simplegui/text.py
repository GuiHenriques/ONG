import PySimpleGUI as sg

tamanhos = ["Pequeno", "Médio", "Grande"]
size = 10
layout = [
    [sg.Text("Nome: ", pad=size, size=10), sg.InputText("", key="nome")],
    [sg.Text("Raça: ", pad=size, size=10), sg.InputText("", key="raca")],
    [sg.Text("Idade: ", pad=size, size=10) ,sg.Slider(range=(1, 20), default_value=1, orientation='h', size=(35,20), key="idade")],
    [sg.Text("Tamanho: ", pad=size, size=10), sg.DropDown(tamanhos, default_value=tamanhos[1], size=10, key="tamanho")],
    [sg.Button("Confirmar", pad=size), sg.Button("Cancelar")],
]

window = sg.Window(f"Dados", layout, size=(500, 300))
            
button, values = window.read()

if button == sg.WINDOW_CLOSED or button == "Cancelar":
    window.close()

if button == "Confirmar":
    window.Close()
    print(values)