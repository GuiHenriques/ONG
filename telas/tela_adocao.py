from datetime import datetime
from telas.abstract_tela import AbstractTela

class TelaAdocao(AbstractTela):

    def tela_opcoes(self):
        print("-------- ADOCAO ----------")
        print("Escolha a opcao")
        print("1 - Adotar Cachorro")
        print("2 - Adotar Gato")
        print("3 - Listar todas as Adoções")
        print("4 - Listar Adocoes por Periodo")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha a opcao: ", [0,1,2,3,4])
        return opcao
    
    def pega_dados_adocao(self):
        print("-------- DADOS ADOCAO ----------")
        cpf = input("CPF do Adotante: ")
        chip = int(input("Chip do Animal: "))
        while True:
            try:
                data_nascimento = input('Data da Adoção (DD/MM/AAAA): ')
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                break
            except ValueError:
                self.mostra_mensagem('Data inválida, insira novamente a data, no formato DD/MM/AAAA. ')
        return {"data": data_f, "cpf": cpf, "chip": chip}
    
    def mostra_adocao(self, adocao):
        print("---------- ADOCAO ------------")
        print("Adotante:", adocao.adotante.nome)
        print("Animal:", adocao.animal.nome)
        print("Data:", adocao.data)

    def assinar_termo_responsa(self):
        print("-------- TERMO DE RESPONSABILIDADE ----------")
        print("1 - Assinar")
        print("2 - Não Assinar")
        
        opcao = self.le_opcao("Escolha a opcao: ", [1,2])
        
        if opcao == 1:
            return True
        else:
            return False
    
    def pega_data(self, msg):
        while True:
            try:
                data_nascimento = input(msg)
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                return data_f
            except ValueError:
                self.mostra_mensagem('Data inválida, insira novamente a data, no formato DD/MM/AAAA. ')

