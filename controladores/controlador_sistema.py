from telas.tela_sistema import TelaSistema
from controladores.controlador_animal import ControladorAnimal
from controladores.controlador_pessoa import ControladorPessoa
from controladores.controlador_adocao import ControladorAdocao
from controladores.controlador_doacao import ControladorDoacao


class ControladorSistema:
    def __init__(self):
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_animal(self):
        return self.__controlador_animal
    
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

    def controle_animal(self):
        self.__controlador_animal.tipo_animal()

    def controle_pessoa(self):
        self.__controlador_pessoa.tipo_pessoa()

    def controle_adocao(self):
        self.__controlador_adocao.abre_tela()

    def controle_doacao(self):
        self.__controlador_doacao.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.controle_animal,
            2: self.controle_pessoa,
            3: self.controle_adocao,
            4: self.controle_doacao,
            0: self.encerra_sistema
        }

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            lista_opcoes[opcao]()
