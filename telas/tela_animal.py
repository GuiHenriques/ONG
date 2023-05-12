class TelaAnimal:
    
    def tela_opcoes(self):
        print("-------- ANIMAIS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Cachorro")
        print("2 - Alterar Cachorro")
        print("3 - Listar Cachorros")
        print("4 - Excluir Cachorro")
        print("5 - Incluir Gato")
        print("6 - Alterar Gato")
        print("7 - Listar Gatos")
        print("8 - Excluir Gato")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_cachorro(self):
        print("-------- DADOS CACHORRO ----------")
        nome = input("Nome: ")
        raca = input("Raca: ")
        idade = input("Idade: ")
        tamanho = input("Tamanho (P, M, G): ")
        return {"nome": nome, "raca": raca, "idade": idade, "tamanho": tamanho}
    
    def pega_dados_gato(self):
        print("-------- DADOS GATO ----------")
        nome = input("Nome: ")
        raca = input("Raca: ")
        idade = input("Idade: ")
        return {"nome": nome, "raca": raca, "idade": idade}

    def mostra_cachorro(self, cachorro):
        print("Chip:", cachorro.chip)
        print("Nome:", cachorro.nome)
        print("Raça:", cachorro.raca)
        print("Idade:", cachorro.idade)
        print("Tamanho:", cachorro.tamanho)
        print("\n")
        
    def mostra_gato(self, gato):
        print("Chip:", gato.chip)
        print("Nome:", gato.nome)
        print("Raça:", gato.raca)
        print("Idade:", gato.idade)
        print("\n")

    def seleciona_animal(self):
        chip = int(input("Chip do animal que deseja selecionar: "))
        return chip
    