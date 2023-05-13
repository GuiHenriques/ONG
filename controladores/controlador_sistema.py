from telas.tela_sistema import TelaSistema
from controladores.controlador_cachorro import ControladorCachorro
from controladores.controlador_gato import ControladorGato
#from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_adocao import ControladorAdocao
from controladores.controlador_doacao import ControladorDoacao


class ControladorSistema:
    def __init__(self):
        self.__controlador_cachorro = ControladorCachorro(self)
        self.__controlador_gato = ControladorGato(self)
        #self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_cachorro(self):
        return self.__controlador_cachorro

    @property
    def controlador_gato(self):
        return self.__controlador_gato

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    # não tem controlador emprestimo na exemplo mvc
    @property
    def controlador_adocao(self):
        return self.__controlador_adocao

    @property
    def controlador_doacao(self):
        return self.__controlador_doacao

    def inicializa_sistema(self):
        self.abre_tela()

    def controle_cachorro(self):
        self.__controlador_cachorro.abre_tela()

    def controle_gato(self):
        self.__controlador_gato.abre_tela()

    def controle_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def controle_adocao(self):
        self.__controlador_adocao.abre_tela()

    def controle_doacao(self):
        self.__controlador_doacao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.controle_cachorro,
            2: self.controle_gato,
            3: self.controle_pessoa,
            4: self.controle_adocao,
            5: self.controle_doacao,
            0: self.encerra_sistema,
        }

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            lista_opcoes[opcao]()
