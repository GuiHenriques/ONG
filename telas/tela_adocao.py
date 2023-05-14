from datetime import datetime


class TelaAdocao:

    def tela_opcoes(self):
        print("-------- ADOCAO ----------")
        print("Escolha a opcao")
        print("1 - Adotar Cachorro")
        print("2 - Adotar Gato")
        print("3 - Listar Adocoes")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_dados_adocao(self):
        print("-------- DADOS ADOCAO ----------")
        data = input("Data da Adoção (DD/MM/AAAA): ")
        data_f = datetime.strptime(data, '%d/%m/%Y').date()
        cpf = input("CPF do Adotante: ")
        chip = int(input("Chip do Animal: "))
        return {"data": data_f, "cpf": cpf, "chip": chip}
    
    def mostra_adocao(self, adocao):
        print("Adotante:", adocao.adotante.nome)
        print("Animal:", adocao.animal.nome)
        print("Data:", adocao.data)
    
    def mostra_mensagem(self, msg):
        print(msg)
