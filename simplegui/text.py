import PySimpleGUI as sg

data = [
    ['John', 25, 'john@example.com'],
    ['Jane', 32, 'jane@example.com'],
    ['Mark', 45, 'mark@example.com'],
]

layout = [
    [sg.Table(values=data, headings=['Name', 'Age', 'Email'], key='-TABLE-')],
    [sg.Button('OK')]
]

window = sg.Window('Table Popup Example', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'OK':
        break

window.close()
