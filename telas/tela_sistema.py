import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None
    
    def tela_opcoes(self):
        layout = self.define_layout_button(["Animais", "Pessoas", "Adocao", "Doacao"])
        
        sg.ChangeLookAndFeel('DarkBlue4')
        self.__window = sg.Window("Sistema ONG", layout, size=(500, 300))
        button, values = self.open()

        if button == sg.WINDOW_CLOSED or button == 'Sair':
            self.close()
            return  0
        
        if button:
            self.close()
            return button

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()