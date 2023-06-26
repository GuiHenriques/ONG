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
            self.close()
            return button
            
    def pega_dados_adocao(self):
        layout = [
            [sg.Text("CPF do Adotante: ", size=15,  pad=10,), sg.InputText("", key="cpf")],
            [sg.Text("Chip do Animal: ", size=15,  pad=10,), sg.InputText("", key="chip")],
            [sg.Text("Data da Adoção:", pad=(10))],
            [sg.Input(key="data", size=(20,1)), sg.CalendarButton("Selecionar Data", close_when_date_chosen=True,  target='data', location=(860, 465), no_titlebar=False, format="%d/%m/%Y")],
            [sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))]
        ]

        self.__window = sg.Window("Dados Adoção", layout, size=(500, 300))

        while True:
            button, values = self.open()

            if button == sg.WINDOW_CLOSED or button == "Sair":
                self.close()
                return None
            
            if self.valor_vazio(values["cpf"]) and self.valor_inteiro(values["chip"]) and self.valor_vazio(values["data"]) and button == "Confirmar":
                self.close()
                data_f = datetime.strptime(values["data"], '%d/%m/%Y').date()
                return {"data": data_f, "cpf": values["cpf"], "chip": int(values["chip"])}
   
    def mostra_adocao(self, dados_adocao):
        todas_adocoes = ""
        for dado in dados_adocao:
            todas_adocoes += "Data: " + dado["data"] + '\n'
            todas_adocoes += "Adotante: " + dado["adotante"] + '\n'
            todas_adocoes += "Animal: " + dado["animal"] + '\n\n'

        sg.Popup('-------- LISTA DE ADOÇÕES ----------', todas_adocoes)

    def assinar_termo_responsa(self):
        layout = [
        [sg.Text("Deseja assinar o termo de responsabilidade?", size=(30,1), pad=(10))],
        [sg.Radio("Sim", "assinatura", key=1, pad=(10)), sg.Radio("Não", "assinatura", key=2, pad=(10))],
        [sg.Text("Motivo: ", size=15,  pad=10,), sg.InputText("", key="motivo")],
        [sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))],
        ]

        self.__window = sg.Window("Termo de Responsabilidade", layout, size=(400, 200))

        button, values = self.open()
        print(button, values)

        if button == "Confirmar" and self.valor_vazio(values["motivo"]):
            print("assinasse")
            return True if values[1] == True else False

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()