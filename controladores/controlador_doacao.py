from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao

class ControladorDoacao():

    def __init__(self, controlador_sistema):
        self.__doacoes = list()
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema

    def incluir_doacao_gato(self):
        self.__controlador_sistema.controlador_pessoa.lista_doadores()
        self.__controlador_sistema.controlador_gato.lista_gatos()
        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        doador = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_doacao["cpf"])
        gato = self.__controlador_sistema.controlador_gato.pega_gato_por_chip(dados_doacao["chip"])

        if (doador and gato):
            doacao = Doacao(dados_doacao["data"], gato, doador, dados_doacao["motivo"])
            self.__doacoes.append(doacao)
            self.__tela_adocao.mostra_mensagem("Adocao realizada com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Dados invalidos")
    
    def incluir_doacao_cachorro(self):
        lista_doadores = self.__controlador_sistema.controlador_pessoa.lista_doadores()
        lista_cachorros = self.__controlador_sistema.controlador_cachorro.lista_cachorros()
        if lista_doadores == None:
            self.__tela_doacao.mostra_mensagem('Não há doadores registrados no sistema! ')
            self.retornar()
        if lista_cachorros == None:
            self.__tela_doacao.mostra_mensagem('Não há cachorros registrados no sistema! ')
            self.retornar()
        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        adotante = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_doacao["cpf"])
        cachorro = self.__controlador_sistema.controlador_cachorro.pega_cachorro_por_chip(dados_doacao["chip"])
        
        if (adotante and cachorro):
            doacao = Doacao(dados_doacao["data"], cachorro, adotante)
            self.__doacoes.append(doacao)
            self.__tela_doacao.mostra_mensagem("Doacao realizada com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Dados invalidos")

    def listar_doacoes(self):
        if len(self.__doacoes) == 0:
            self.__tela_doacao.mostra_mensagem("Nenhuma doacao cadastrada")
        for doacao in self.__doacoes:
            self.__tela_doacao.mostra_doacao(doacao)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao_cachorro,
            2: self.incluir_doacao_gato,
            3: self.listar_doacoes,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            