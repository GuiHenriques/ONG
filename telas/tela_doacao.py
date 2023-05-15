from datetime import datetime
from telas.abstract_tela import AbstractTela

class TelaDoacao(AbstractTela):

    def tela_opcoes(self):
        print("-------- DOACAO ----------")
        print("Escolha a opcao")
        print("1 - Doar Cachorro")
        print("2 - Doar Gato")
        print("3 - Listar Doações (Relatório)")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha a opcao: ", [0, 1, 2, 3,])
        return opcao

    def pega_dados_doacao(self):
        print("-------- DADOS DOACAO ----------")
        cpf = input("CPF do Doador: ")
        chip = int(input("Chip do Animal: "))
        motivo = input("Motivo da Doação: ")
        while True:
            try:
                data_nascimento = input('Data da doacao (DD/MM/AAAA): ')
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                break
            except ValueError:
                self.mostra_mensagem('Data inválida, insira novamente a data, no formato DD/MM/AAAA. ')
        return {"data": data_f, "cpf": cpf, "chip": chip, "motivo": motivo}

    def mostra_doacao(self,doacao):
        print("---------- DOAÇÕES ------------")
        print("Doador:", doacao.doador.nome)
        print("Animal:", doacao.animal.nome)
        print("Data:", doacao.date)

    def seleciona_pessoa_por_cpf(self):
        cpf = input('Insira o cpf da pessoa: ')
        return cpf


