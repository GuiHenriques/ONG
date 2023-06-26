from datetime import datetime
from telas.abstract_tela import AbstractTela
import PySimpleGUI as sg


class TelaDoacao(AbstractTela):

    def tela_opcoes(self):
        layout = self.define_layout_button([
                "Doar Animal",
                "Listar todas as Doações",
                "Listar Doações por Período",])

        self.__window = sg.Window("Doação", layout, size=(500, 300))
        button, values = self.open()

        if button == "Sair" or button == sg.WINDOW_CLOSED:
            self.close()
            return 0

        if button:
            self.close()
            return button

    def pega_dados_doacao(self):
        layout = [
            [sg.Text("Data da Doação:", pad=(10))],
            [sg.Input("", key="data", size=(20,1)), sg.CalendarButton("Selecionar Data", close_when_date_chosen=True,  target='data', location=(860, 465), no_titlebar=False, format="%d/%m/%Y")],
            [sg.Text("Motivo da Doação:", size=15, pad=10), sg.Multiline("", key="motivo", size=(25,3))],
            [sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))],
        ]

        self.__window = sg.Window("Dados Doação", layout, size=(500, 300))

        while True:
            button, values = self.open()

            if button == sg.WINDOW_CLOSED or button == "Sair":
                self.close()
                return None
            
            if self.valor_vazio(values["data"]) and self.valor_vazio(values["motivo"]) and button == "Confirmar":
                data_f = datetime.strptime(values["data"], '%d/%m/%Y').date()
                self.close()
                return {"data": data_f, "motivo": values["motivo"]}

    def mostra_doacao(self, dados_doacao):
        todas_doacoes = ""
        for dado in dados_doacao:
            todas_doacoes += "Data: " + dado["data"] + '\n'
            todas_doacoes += "Doador: " + dado["adotante"] + '\n'
            todas_doacoes += "Animal: " + dado["animal"] + '\n'
            todas_doacoes += "Motivo: " + dado["motivo"] + '\n\n'

        sg.Popup('-------- LISTA DE ADOÇÕES ----------', todas_doacoes)
    
    def seleciona_pessoa_por_cpf(self):
        cpf = input('Insira o cpf da pessoa: ')
        return cpf

    def pega_datas(self):
        layout = [
            [sg.Text("Data Inicial:", pad=(10), key="data_inicial"), sg.CalendarButton("Selecionar Data", close_when_date_chosen=True,  target='data_inicial', location=(860, 465), format="%d/%m/%Y")],
            [sg.Text("Data Final:", pad=(10), key="data_final"), sg.CalendarButton("Selecionar Data", close_when_date_chosen=True,  target='data_final', location=(860, 465), format="%d/%m/%Y")],
            [sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))],
        ]

        self.__window = sg.Window("Definir Período", layout, size=(500, 300))

        while True:
            button, values = self.open()
            self.close()

            if button == sg.WINDOW_CLOSED or button == "Sair":
                return None, None
            
            if self.valor_vazio(values["data_inicial"]) and self.valor_vazio(values["data_final"]):
                data_inicial = datetime.strptime(values["data_inicial"], '%d/%m/%Y').date()
                data_final = datetime.strptime(values["data_final"], '%d/%m/%Y').date()
                return data_inicial, data_final
            
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()