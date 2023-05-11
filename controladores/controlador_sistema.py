from telas.tela_sistema import TelaSistema
from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_doacao import ControladorDoacao
from controladores.controlador_adocao import ControladorAdocao

class ControladorSistema():
    
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    @property
    def controlador_adocao(self):
        return self.__controlador_adocao
    
    @property
    def controlador_doacao(self):
        return self.__controlador_doacao
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_pessoas(self):
        self.__controlador_pessoa.abre_tela()

    def cadastra_doacao(self):
        self.__controlador_doacao.abre_tela()

    def cadastra_adocao(self):
        self.__controlador_adocao.abre_tela()

    def cadastra_animais(self):
        pass

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_doacao, 2: self.cadastra_adocao, 3: self.cadastra_pessoas,
                        4: self.cadastra_animais, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
