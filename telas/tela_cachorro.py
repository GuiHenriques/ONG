from telas.abstract_tela import AbstractTela
from datetime import datetime


class TelaCachorro(AbstractTela):
    
    def tela_opcoes(self):
        print("-------- CACHORROS ----------")
        print("1 - Incluir Cachorro")
        print("2 - Alterar Cachorro")
        print("3 - Listar Cachorros")
        print("4 - Excluir Cachorro")
        print("5 - Adicionar Vacina")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha a opcao: ", [0,1,2,3,4,5])
        return opcao
    
    def pega_dados_cachorro(self):
        print("-------- DADOS CACHORRO ----------")
        nome = input("Nome: ")
        raca = input("Raça: ")
        idade = input("Idade: ")
        tamanho = input("Tamanho (P, M, G): ")
        return {"nome": nome, "raca": raca, "idade": idade, "tamanho": tamanho}

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
            
        tipo = input("Tipo: ").capitalize()
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
    
    def mostra_cachorro(self, cachorro):
        print("---------- CACHORRO ------------")
        print("Chip:", cachorro.chip)
        print("Nome:", cachorro.nome)
        print("Raça:", cachorro.raca)
        print("Idade:", cachorro.idade)
        print("Tamanho:", cachorro.tamanho)
        print("Vacinas:", end=" ")
        if len(cachorro.vacinas) == 0:
            print("Sem vacinas")
        for vacina in cachorro.vacinas:
            print(vacina.tipo, end=", ")
        print("\n")
    
    def seleciona_cachorro(self):
        chip = input("Chip do cachorro que deseja selecionar: ")
        return chip