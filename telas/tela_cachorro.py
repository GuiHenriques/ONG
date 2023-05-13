class TelaCachorro:
    
    def tela_opcoes(self):
        print("-------- CACHORROS ----------")
        print("1 - Incluir Cachorro")
        print("2 - Alterar Cachorro")
        print("3 - Listar Cachorros")
        print("4 - Excluir Cachorro")
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
    
    def mostra_cachorro(self, cachorro):
        print("Chip:", cachorro.chip)
        print("Nome:", cachorro.nome)
        print("Raça:", cachorro.raca)
        print("Idade:", cachorro.idade)
        print("Tamanho:", cachorro.tamanho)
        print("\n")
    
    def seleciona_cachorro(self):
        chip = int(input("Chip do cachorro que deseja selecionar: "))
        return chip