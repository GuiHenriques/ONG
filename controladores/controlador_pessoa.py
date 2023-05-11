from telas.tela_pessoa import TelaPessoa
from controladores.controlador_sistema import ControladorSistema

class ControladorPessoa():

    def __init__(self, controlador_sistema: ControladorSistema):
        self.__adotantes = list()
        self.__doadores = list()
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    def incluir_adotante(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_adotante()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adotante, 2: self.altera_adotante, 3: self.lista_adotante, 4: self.excluir_adotante,
                        5: self.incluir_doador, 6: self.altera_doador, 7: self.lista_doador, 8: self.excluir_doador,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_livro.tela_opcoes()]()