from telas.abstract_tela import AbstactTela
from datetime import datetime

    
class TelaAnimal(AbstactTela):

    def tela_opcoes(self, animal):
        print(f"-------- {animal} --------")
        print(f"1 - Incluir {animal}")
        print(f"2 - Alterar {animal}")
        print(f"3 - Listar {animal}s")
        print(f"4 - Listar {animal}s disponíveis")
        print(f"5 - Excluir {animal}")
        print(f"0 - Retornar")

        opcao = self.le_opcao("Escolha a opção: ", [1, 2, 3, 4, 5, 0])
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
        print("Selecione o tipo de animal")
        print("1 - Cachorro")
        print("2 - Gato")
        tipo = self._le_numero_inteiro("Escolha a opção: ", [1, 2])
        animal = "Cachorro" if tipo == 1 else "Gato"
        return animal
    
    def mostra_animal(self, dados_animal):
        print("-------- Animal --------")
        print(f"Nome: {dados_animal['nome']}")
        print(f"Raça: {dados_animal['raca']}")
        
        if "tamanho" in dados_animal:
            print(f"Tamanho: {dados_animal['tamanho']}")
    