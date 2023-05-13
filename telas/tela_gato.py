class TelaGato:

    def tela_opcoes(self):
        print("-------- GATOS ----------")
        print("1 - Incluir Gato")
        print("2 - Alterar Gato")
        print("3 - Listar Gatos")
        print("4 - Excluir Gato")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_dados_gato(self):
        print("-------- DADOS GATO ----------")
        nome = input("Nome: ")
        raca = input("Raca: ")
        idade = input("Idade: ")
        return {"nome": nome, "raca": raca, "idade": idade}

    def mostra_gato(self, gato):
        print("Chip:", gato.chip)
        print("Nome:", gato.nome)
        print("Raça:", gato.raca)
        print("Idade:", gato.idade)
        print("\n")

    def seleciona_gato(self):
        chip = int(input("Chip do gato que deseja selecionar: "))
        return chip
    