import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):

    def tela_opcoes(self):

        layout = self.define_layout_button(["Animais", "Pessoas", "Adocao", "Doacao"])

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
                    