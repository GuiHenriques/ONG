from telas.abstract_tela import AbstractTela
from datetime import datetime

    
class TelaAnimal(AbstractTela):

    def tela_opcoes(self, animal):
        print(f"-------- {animal} --------")
        print(f"1 - Incluir {animal}")
        print(f"2 - Alterar {animal}")
        print(f"3 - Listar {animal}s")
        print(f"4 - Listar {animal}s disponíveis")
        print(f"5 - Excluir {animal}")
        print("6 - Adicionar Vacina")
        print(f"0 - Retornar")

        opcao = self.le_opcao("Escolha a opção: ", [1, 2, 3, 4, 5, 6, 0])
        return opcao
    
    def pega_dados_animal(self, animal):
        print(f"-------- Dados {animal} --------")
        nome = input("Nome: ")
        raca = input("Raça: ")
        
        if animal == "Cachorro":
            tamanho = input("Tamanho: ")
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

        while True:
            try:
                data = input("Data (DD/MM/AAAA): ")
                data_f = datetime.strptime(data, '%d/%m/%Y').date()
                break
            except ValueError:
                self.mostra_mensagem('Data inválida, insira a data no formato DD/MM/AAAA. ')

        return {"tipo": tipo, "data": data_f}
    
    def seleciona_animal(self):
        chip = input("Chip do animal: ")
        return chip

    def seleciona_tipo_animal(self):
        print("Selecione o tipo de animal")
        print("1 - Cachorro")
        print("2 - Gato")
        tipo = self.le_opcao("Escolha a opção: ", [1, 2])
        animal = "Cachorro" if tipo == 1 else "Gato"
        return animal
    
    def mostra_animal(self, dados_animal):
        print("-------- Animal --------")
        print(f"Chip: {dados_animal['chip']}")
        print(f"Nome: {dados_animal['nome']}")
        print(f"Raça: {dados_animal['raca']}")
        if "tamanho" in dados_animal:
            print(f"Tamanho: {dados_animal['tamanho']}")
        print(f"Vacinas: ", end="")
        if len(dados_animal['vacinas']) == 0:
            print(" Nenhuma")
        for vacina in dados_animal['vacinas']:
            print(vacina.tipo, end=", ")
        print()
        
    