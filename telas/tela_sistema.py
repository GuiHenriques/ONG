from telas.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):

    def tela_opcoes(self):

        print("-------- SisONG ---------")
        print("Escolha sua opcao")
        print("1 - Gerenciar Cachorros")
        print("2 - Gerenciar Gatos")
        print("3 - Gerenciar Pessoas")
        print("4 - Realizar Adoção")
        print("5 - Realizar Doação")
        print("0 - Finalizar Sistema")
        
        opcao = self.le_opcao("Escolha a opcao: ", [0,1,2,3,4,5])
        return opcao
