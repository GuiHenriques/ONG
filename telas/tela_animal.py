class TelaAnimal:
    
    def tela_opcoes(self):
        print("-------- ANIMAIS ----------")
        print("Escolha a opcao")
        print("1 - Incluir Animal")
        print("2 - Alterar Animal")
        print("3 - Listar Animais")
        print("4 - Excluir Animal")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao