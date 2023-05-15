from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao

class ControladorDoacao():


    def __init__(self, controlador_sistema):
        self.__doacoes = list()
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema


    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao,
            2: self.alterar_doacao,
            3: self.listar_doacoes,
            4: self.excluir_doacao,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()

    def incluir_doacao(self):
        self.__controlador_sistema.controlador_pessoa.lista_doadores()
        cpf_doador = self.__tela_doacao.seleciona_pessoa_por_cpf()
        doador = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(cpf_doador)
        animal = self.__tela_doacao.seleciona_animal()
        if animal == 'cachorro':
            self.__controlador_sistema.controlador_cachorro.lista_cachorros()

        if animal == 'gato':
            self.__controlador_

    def alterar_doacao(self):
        pass

    def listar_doacoes(self):
        pass

    def excluir_doacao(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

