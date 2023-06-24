import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela
from datetime import datetime


class TelaAnimal(AbstractTela):
    def __init__(self):
        self.__window = None

    def init_opcoes(self, animal):
        key = 1
        layout = [
            [sg.Button(f"Incluir {animal}", size=(22,1), pad=(25,20), key=1), sg.Button(f"Listar {animal}s disponíveis", size=(22,1), pad=(25,20), key=4)],
            [sg.Button(f"Alterar {animal}", size=(22,1), pad=(25,20), key=2), sg.Button(f"Adicionar Vacina", size=(22,1), pad=(25,20), key=6)],
            [sg.Button(f"Listar {animal}s", size=(22,1), pad=(25,20), key=3), sg.Button("Voltar", size=(22,1), pad=(25,20))],
            [sg.Button(f"Excluir {animal}", size=(22,1), pad=(25,20), key=5)]
        ]
        self.__window = sg.Window(f"{animal}s", layout, size=(500, 300))

    def tela_opcoes(self, animal):
        self.init_opcoes(animal)

        button, values = self.open()

        if button == sg.WINDOW_CLOSED or button == "Voltar":
            self.close()
            return 0
        
        if button:
            self.close()
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

        button, values = self.open()

        if button == sg.WINDOW_CLOSED or button == "Cancelar":
            self.close()
            return None

        if button == "Confirmar":
            self.close()
            print(values)
            return values

    def pega_dados_vacina(self):
        print("-------- Dados Vacina --------")
        print("1 - Raiva")
        print("2 - Lepitospirose")
        print("3 - Hepatite Infecciosa")
        print("4 - Todas as Vacinas")

        tipo = self.le_opcao("Escolha a opção: ", [1, 2, 3, 4])

        match tipo:
            case 1:
                tipo = "Raiva"
            case 2:
                tipo = "Lepitospirose"
            case 3:
                tipo = "Hepatite Infecciosa"
            case 4:
                tipo = "Todas"

        data = input("Data (DD/MM/AAAA): ")

        return {"tipo": tipo, "data": data}

    def seleciona_animal(self):
        chip = input("Chip do animal: ")
        return chip

    def seleciona_tipo_animal(self):
        layout = self.define_layout_button(["Cachorro", "Gato"])

        self.__window = sg.Window("Tipo de Animal", layout, size=(500, 300))

        button, values = self.open()

        if button == sg.WINDOW_CLOSED or button == 0:
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
