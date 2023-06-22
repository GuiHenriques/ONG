import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def init_opcoes(self):
        layout = self.define_layout_button(["Animais", "Pessoas", "Adocao", "Doacao"])
        self.__window = sg.Window("Sistema ONG", layout, size=(500, 300))

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()

        if button == sg.WINDOW_CLOSED:
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
    
    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)