import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela
from datetime import datetime


class TelaAnimal(AbstractTela):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self, animal):
        layout = [
            [sg.Button(f"Incluir {animal}", size=(22,1), pad=(25,20), key=1), sg.Button(f"Listar {animal}s disponíveis", size=(22,1), pad=(25,20), key=4)],
            [sg.Button(f"Alterar {animal}", size=(22,1), pad=(25,20), key=2), sg.Button(f"Adicionar Vacina", size=(22,1), pad=(25,20), key=6)],
            [sg.Button(f"Listar {animal}s", size=(22,1), pad=(25,20), key=3), sg.Button("Voltar", size=(22,1), pad=(25,20))],
            [sg.Button(f"Excluir {animal}", size=(22,1), pad=(25,20), key=5)]
        ]
        self.__window = sg.Window(f"{animal}s", layout, size=(500, 300))

        button, values = self.open()
        self.close()

        if button == sg.WINDOW_CLOSED or button == "Voltar":
            return 0
        
        if button:
            return button

    def pega_dados_animal(self, animal):
        size = 10

        layout = [
            [sg.Text("Nome: ", pad=size, size=size), sg.InputText("", key="nome")],
            [sg.Text("Raça: ", pad=size, size=size), sg.InputText("", key="raca")],
            [sg.Text("Idade: ", pad=size, size=size),
            sg.Slider(range=(1, 20),default_value=1,orientation="h",size=(35, 20),key="idade",)],
        ]

        if animal == "Cachorro":
            tamanhos = ["Pequeno", "Médio", "Grande"]
            layout.append([sg.Text("Tamanho: ", pad=size, size=size),
                           sg.DropDown(tamanhos, default_value=tamanhos[1], size=size, key="tamanho"),])

        layout.append([sg.Button("Confirmar", pad=size), sg.Button("Cancelar")])

        self.__window = sg.Window(f"Dados {animal}", layout, size=(500, 300))

        while True:
            button, values = self.open()
            
            if button == sg.WINDOW_CLOSED or button == "Cancelar":
                return None
            
            if self.valores_vazios(values):
                if button == "Confirmar":
                    self.close()    
                    return values

    def pega_dados_vacina(self):
        elementos = ["Raiva", "Lepitospirose", "Hepatite Infecciosa", "Todas as Vacinas"]
        layout = [
            [sg.Radio("Raiva", "RD1", key=1)],
            [sg.Radio("Lepitospirose", "RD1", key=2)],
            [sg.Radio("Hepatite Infecciosa", "RD1", key=3)],
            [sg.Radio("Todas as Vacinas", "RD1", key=4)],
            [sg.Text("Data de Aplicação da Vacina:", pad=(10, 10))],
            [sg.Input(key="data", size=(20,1)), sg.CalendarButton("Selecionar Data", close_when_date_chosen=True,  target='data', location=(860, 465), no_titlebar=False, format="%d/%m/%Y")],
            [sg.Button("Confirmar", size=(10,1), pad=(10)), sg.Button("Sair", size=(10,1), pad=(10))]
        ]

        self.__window = sg.Window("Vacinas", layout, size=(500, 300))
        
        while True:
            button, values = self.open()

            if button == sg.WINDOW_CLOSED or button == "Sair":
                self.close()
                return None
            
            if self.valor_vazio_radio([values[x] for x in range(1, 5)]) and self.valor_vazio(values["data"]):
                self.close()
                break
        
        if values[4]:
            tipo = "Todas"
        elif values[3]:
            tipo = "Hepatite Infecciosa"
        elif values[2]:
            tipo = "Lepitospirose"
        elif values[1]:
            tipo = "Raiva"

        return {"tipo": tipo, "data": values["data"]}

    def seleciona_animal(self):
        layout = [
            [sg.Text("Chip do Animal: ")],
            [sg.Spin([i for i in range(1, 100)], initial_value=1, key="chip", size=(6))],
            [sg.Button("Confirmar", size=(10,1), pad=(2, 10))]
        ]

        self.__window = sg.Window("Selecionar Animal", layout, size=(200,150))

        button, values = self.open()
        self.close()

        if button == sg.WINDOW_CLOSED:
            return None

        if button == "Confirmar":
            return values["chip"]

    def seleciona_tipo_animal(self):
        layout = self.define_layout_button(["Cachorro", "Gato"])

        self.__window = sg.Window("Tipo de Animal", layout, size=(500, 300))

        button, values = self.open()

        if button == sg.WINDOW_CLOSED or button == "Sair":
            self.close()
            return None

        self.close()
        return "Cachorro" if button == 1 else "Gato"

    def mostra_animal(self, dados_animal):
        width = [4, 11, 11, 4, 8, 11] if len(dados_animal[0]) == 6 else [5, 12, 13, 6, 13]
        layout = [
            [sg.Table(values=dados_animal[1:], headings=dados_animal[0], num_rows=max(len(dados_animal), 8), row_height=25, justification='center', auto_size_columns=False, col_widths=width)],
            [sg.Txt("", size=20), sg.Button("Ok", size=(10,1), pad=(10))]
        ]

        self.__window = sg.Window("Lista de Animais", layout, size=(500, 300))

        button, values = self.open()

        if button == sg.WINDOW_CLOSED:
            exit(0)

        if button == "Ok":
            self.close()
            return

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
