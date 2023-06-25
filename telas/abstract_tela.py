import PySimpleGUI as sg


class AbstractTela:

    def define_layout_button(self, elementos):
        layout = [
            [sg.Button(elemento, size=(20,1), pad=(10), key=key+1)] for key, elemento in enumerate(elementos)
        ]
        layout.append([sg.Button("Sair", size=(20,1), pad=(10))])
        return layout
    
    def define_layout_radio(self, elementos):
        layout = [
            [sg.Radio(elemento, "RD1", key=key+1)] for key, elemento in enumerate(elementos)
        ]
        layout.append([sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))])
        return layout

    def valores_vazios(self, valores):
        for valor in valores.values():
            if valor == "":
                self.mostra_mensagem("Erro", "Valores não podem ser vazios")
                return False
        return True

    def valor_vazio(self, valor):
        if valor == "":
            self.mostra_mensagem("Erro", "Valores não podem ser vazios")
            return False
        return True
    
    def valor_vazio_radio(self, valores):
        for valor in valores:
            if valor == True:
                return True
        self.mostra_mensagem("Erro", "Selecione uma opção do Radio Button")
        return False


    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(mensagem, title=titulo)
    