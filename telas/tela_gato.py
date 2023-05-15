from telas.abstract_tela import AbstractTela
from datetime import datetime


class TelaGato(AbstractTela):

    def tela_opcoes(self):
        print("-------- GATOS ----------")
        print("1 - Incluir Gato")
        print("2 - Alterar Gato")
        print("3 - Listar Gatos")
        print("4 - Excluir Gato")
        print("5 - Adicionar Vacina")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha a opcao: ", [0,1,2,3,4,5])
        return opcao
    
    def pega_dados_gato(self):
        print("-------- DADOS GATO ----------")
        nome = input("Nome: ")
        raca = input("Raça: ")
        
        while True:
            try:
                idade = input("Idade: ")
                idade = int(idade)
                if idade < 0:
                    raise ValueError
                break
            except ValueError:
                self.mostra_mensagem("Idade inválida")
                
        return {"nome": nome, "raca": raca, "idade": idade}

    def pega_dados_vacina(self):
        print("-------- DADOS VACINA ----------")
        print("1 - Raiva")
        print("2 - Leptospirose")
        print("3 - Hepatite Infecciosa")

        vacinas_validas = ["Raiva", "Leptospirose", "Hepatite Infecciosa"]
        while True:
            tipo = input("Tipo: ").capitalize()
            if tipo in vacinas_validas or tipo in ["1", "2", "3"]:
                break
            else:
                self.mostra_mensagem("Tipo inválido")
        
        if tipo.isnumeric():
            if tipo == "1":
                tipo = "Raiva"
            elif tipo == "2":
                tipo = "Leptospirose"
            elif tipo == "3":
                tipo = "Hepatite Infecciosa"
        
        data = input("Data (DD/MM/AAAA): ")
        data_f = datetime.strptime(data, '%d/%m/%Y').date()
        return {"tipo": tipo, "data": data_f}

    def mostra_gato(self, gato):
        print("---------- GATO ------------")
        print("Chip:", gato.chip)
        print("Nome:", gato.nome)
        print("Raça:", gato.raca)
        print("Idade:", gato.idade)
        print("Vacinas:", end=" ")
        if len(gato.vacinas) == 0:
            print("Sem vacinas")
        for vacina in gato.vacinas:
            print(vacina.tipo, end=', ')
        print("\n")

    def seleciona_gato(self):
        chip = input("Chip do gato que deseja selecionar: ")
        
        return chip
    