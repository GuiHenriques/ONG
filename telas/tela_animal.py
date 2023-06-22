import PySimpleGUI as sg
from telas.abstract_tela import AbstractTela
from datetime import datetime


class TelaAnimal(AbstractTela):

    def __init__(self):
        self.__window = None

    def init_opcoes(self, animal):
        layout = self.define_layout_button([
                f"Incluir {animal}", # 1
                f"Alterar {animal}", # 2
                f"Listar {animal}s", # 3
                f"Listar {animal}s disponíveis", # 4
                f"Excluir {animal}", # 5
                "Adicionar Vacina", # 6
            ])
        self.__window = sg.Window(f"{animal}s", layout, size=(500, 300))

    def tela_opcoes(self, animal):
        self.init_opcoes(animal)

        button, values = self.open()

        if button:
            self.close()
            return button
    
        button, values = self.open()

        if button == sg.WINDOW_CLOSED or button == "sair":
            self.close()
            return 0

    def pega_dados_animal(self, animal):
        print(f"-------- Dados {animal} --------")
        nome = input("Nome: ")
        raca = input("Raça: ")

        if animal == "Cachorro":
            # layout.append(dropdown_tamanho)
            # tamanho = input("Tamanho: ")
            
            return {"nome": nome, "raca": raca, "tamanho": tamanho}

        return {"nome": nome, "raca": raca}

    def pega_dados_vacina(self):
        print("-------- Dados Vacina --------")
        print("1 - Raiva")
        print("2 - Lepitospirose")
        print("3 - Hepatite Infecciosa")
        print("4 - Todas as Vacinas")

        tipo = self.le_opcao("Escolha a opção: ", [1, 2, 3, 4])

        '''match tipo:
            case 1:
                tipo = "Raiva"
            case 2:
                tipo = "Lepitospirose"
            case 3:
                tipo = "Hepatite Infecciosa"
            case 4:
                tipo = "Todas"'''

        if tipo == 1:
            tipo = "Raiva"
        elif tipo == 2:
            tipo = "Lepitospirose"
        elif tipo == 3:
            tipo = "Hepatite Infecciosa"
        elif tipo == 4:
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
        print("-------- Animal --------")
        print(f"Chip: {dados_animal['chip']}")
        print(f"Nome: {dados_animal['nome']}")
        print(f"Raça: {dados_animal['raca']}")
        if "tamanho" in dados_animal:
            print(f"Tamanho: {dados_animal['tamanho']}")
        print(f"Vacinas: ", end="")
        if len(dados_animal["vacinas"]) == 0:
            print(" Nenhuma")
        for vacina in dados_animal["vacinas"]:
            print(vacina.tipo, end=", ")
        print()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)