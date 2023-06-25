from datetime import datetime
from telas.abstract_tela import AbstractTela

class TelaDoacao(AbstractTela):

    def tela_opcoes(self):
        print("-------- Doação ----------")
        print("1 - Doar Animal")
        print("2 - Listar todas as Doações")
        print("3 - Listar Doações por Periodo")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha a opcao: ", [0, 1, 2, 3, 4])
        return opcao

    def pega_dados_doacao(self):
        print("-------- Dados Doação ----------")
        while True:
            try:
                data_nascimento = input('Data da doacao (DD/MM/AAAA): ')
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                break
            except ValueError:
                self.mostra_mensagem('Data inválida, insira novamente a data, no formato DD/MM/AAAA. ')
        motivo = input("Motivo da Doação: ")
        return {"data": data_f, "motivo": motivo}

    def mostra_doacao(self, dados_doacao):
        print("---------- Doação ------------")
        print("Data:", dados_doacao["data"])
        print("Doador:", dados_doacao["doador"])
        print("Animal:", dados_doacao["animal"])
        print("Motivo:", dados_doacao["motivo"])

    def seleciona_pessoa_por_cpf(self):
        cpf = input('Insira o cpf da pessoa: ')
        return cpf

    def pega_data(self, msg):
        while True:
            try:
                data_nascimento = input(msg)
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                return data_f
            except ValueError:
                self.mostra_mensagem('Data inválida, insira novamente a data, no formato DD/MM/AAAA. ')

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()