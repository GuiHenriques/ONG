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

    def mostra_cachorro(self, dados_cachorro):
        print("Nome:", dados_cachorro["nome"])
        print("Raça:", dados_cachorro["raca"])
        print("Idade:", dados_cachorro["idade"])
        print("Tamanho:", dados_cachorro["tamanho"])
        
    def mostra_gato(self, dados_gato):
        print("Nome:", dados_gato["nome"])
        print("Raça:", dados_gato["raca"])
        print("Idade:", dados_gato["idade"])
