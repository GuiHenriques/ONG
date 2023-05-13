from telas.tela_adocao import TelaAdocao
from entidades.adocao import Adocao


class ControladorAdocao():
    def __init__(self, controlador_sistema):
        self.__adocoes = list()
        #self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    def incluir_adocao(self):


