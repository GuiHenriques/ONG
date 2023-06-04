from telas.abstract_tela import AbstractTela

class TelaSistema(AbstractTela):

    def tela_opcoes(self):

        print("-------- SisONG ---------")
        print("Escolha sua opcao")
        print("1 - Animais")
        print("2 - Pessoas")
        print("3 - Adoção")
        print("4 - Doação")
        print("0 - Finalizar Sistema")
        
        opcao = self.le_opcao("Escolha a opcao: ", [0,1,2,3,4,5])
        return opcao
