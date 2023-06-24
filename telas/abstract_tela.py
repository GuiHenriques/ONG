import PySimpleGUI as sg


class AbstractTela:

    def le_opcao(self, mensagem="", ints_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError 
                return valor_int
            except ValueError: 
                print("Valor inválido")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)    

    def define_layout_button(self, elementos):
        layout = [
            [sg.Button(elemento, size=(20,1), pad=(10), key=key+1)] for key, elemento in enumerate(elementos)
        ]
        layout.append([sg.Button("Sair", size=(20,1), pad=(10))])
        return layout
    
    def define_layout_radio(self, elementos):
        ...

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.Popup(mensagem, title=titulo)
    