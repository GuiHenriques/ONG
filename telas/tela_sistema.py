import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):

    def tela_opcoes(self):

        layout = [
            [sg.Button("Animais", size=(20,1), pad=(10), key="animais")],
            [sg.Button("Pessoas", size=(20,1), pad=(10), key="pessoas")],
            [sg.Button("Adoção", size=(20,1), pad=(10), key="adocao")],
            [sg.Button("Doação", size=(20,1), pad=(10), key="doacao")],
            [sg.Button("Finalizar Sistema", button_color='red', size=(20,1), pad=(10), key="sair")],
        ]

        window = sg.Window("Data Entry Form", layout, size=(500, 300))

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "sair":
                window.close()
                return  0
            
            if event:
                window.close()
                
                match event:
                    case "animais":
                        return 1
                    case "pessoas":
                        return 2
                    case "adocao":
                        return 3
                    case "doacao":
                        return 4
                    