from telas.abstract_tela import AbstractTela

class TelaDoacao(AbstractTela):

    def tela_opcoes(self):
        print("-------- DOACAO ----------")
        print("Escolha a opcao")
        print("1 - Registrar Doação")
        print("2 - Alterar Doação")
        print("3 - Listar Doações")
        print("4 - Excluir Doação")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha a opcao: ", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_doacao(self):
        print("-------- DADOS DOACAO ----------")
        data = input("Data da Doação (DD/MM/AAAA): ")
        data_f = datetime.strptime(data, '%d/%m/%Y').date()
        cpf = input("CPF do Doador: ")
        chip = int(input("Chip do Animal: "))
        return {"data": data_f, "cpf": cpf, "chip": chip}

    def seleciona_pessoa_por_cpf(self):
        cpf = input('Insira o cpf da pessoa: ')
        return cpf

    def seleciona_animal(self):
        while True:
            animal = input('Vai doar um cachorro ou um gato? ')
            if animal != 'gato' and animal != 'cachorro':
                print()
                print('Resposta inválida! ')
                print()
            return animal

