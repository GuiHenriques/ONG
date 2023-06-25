import PySimpleGUI as sg
from datetime import datetime
from telas.abstract_tela import AbstractTela


class TelaAdocao(AbstractTela):
    def tela_opcoes(self):
        layout = self.define_layout_button([
                "Adotar Animal",
                "Listar todas as Adoções",
                "Listar Adoções por Período",])

        self.__window = sg.Window("Adoção", layout, size=(500, 300))
        button, values = self.open()

        if button == "Sair" or button == sg.WINDOW_CLOSED:
            self.close()
            return 0

        if button:
            print(button)
            self.close()

            return button
            
    def pega_dados_adocao(self):
        layout = [
            [sg.Text("CPF do Adotante: ", size=15), sg.InputText("", key="cpf")],
            [sg.Text("Chip do Animal: ", size=15), sg.InputText("", key="chip")],
            [sg.Text("Data da Adoção:", pad=(10, 10))],
            [sg.Input(key="data", size=(20,1)), sg.CalendarButton("Selecionar Data", close_when_date_chosen=True,  target='data', location=(860, 465), no_titlebar=False, format="%d/%m/%Y")],
            [sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))]
        ]

        self.__window = sg.Window("Dados Adoção", layout, size=(500, 300))

        while True:
            button, values = self.open()
            print(values)

            if button == sg.WINDOW_CLOSED or button == "Sair":
                self.close()
                return None
            
            if self.valor_vazio(values["cpf"]) and self.valor_vazio(values["chip"]) and self.valor_vazio(values["data"]):
                self.close()
                break
        
        return {"data": data_f, "cpf": cpf, "chip": chip}

    def mostra_adocao(self, dados_adocao):
        print("---------- ADOCAO ------------")
        print("Data:", dados_adocao["data"])
        print("Adotante:", dados_adocao["adotante"])
        print("Animal:", dados_adocao["animal"])

    def assinar_termo_responsa(self):
        print("-------- TERMO DE RESPONSABILIDADE ----------")
        print("1 - Assinar")
        print("2 - Não Assinar")

        opcao = self.le_opcao("Escolha a opcao: ", [1, 2])

        if opcao == 1:
            return True
        else:
            return False

    def pega_data(self, msg):
        sg.popup_get_date(msg)
        

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()