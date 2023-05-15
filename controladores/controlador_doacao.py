from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao

class ControladorDoacao():

    def __init__(self, controlador_sistema):
        self.__doacoes = list()
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema

    def incluir_doacao_gato(self):
        lista_doadores = self.__controlador_sistema.controlador_pessoa.lista_doadores()
        lista_gatos = self.__controlador_sistema.controlador_gato.lista_gatos()

        if not lista_doadores or not lista_gatos:
            self.__tela_doacao.mostra_mensagem("Nao ha doadores ou gatos cadastrados")
            self.retornar()

        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        doador = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_doacao["cpf"])
        gato = self.__controlador_sistema.controlador_gato.pega_gato_por_chip(dados_doacao["chip"])

        if (doador and gato):
            doacao = Doacao(dados_doacao["data"], gato, doador, dados_doacao["motivo"])
            self.__doacoes.append(doacao)
            self.__tela_doacao.mostra_mensagem("Adocao realizada com sucesso!")
        else:
            self.__tela_doacao.mostra_mensagem("Dados invalidos")
    
    def incluir_doacao_cachorro(self):
        lista_doadores = self.__controlador_sistema.controlador_pessoa.lista_doadores()
        lista_cachorros = self.__controlador_sistema.controlador_cachorro.lista_cachorros()

        if lista_doadores is None:
            self.__tela_doacao.mostra_mensagem("Nao ha doadores cadastrados")
            self.abre_tela()

        if lista_cachorros is None:
            self.__tela_doacao.mostra_mensagem("Nao ha cachorros cadastrados")
            self.abre_tela()


        dados_doacao = self.__tela_doacao.pega_dados_doacao()

        doador = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_doacao["cpf"])
        cachorro = self.__controlador_sistema.controlador_cachorro.pega_cachorro_por_chip(dados_doacao["chip"])
        motivo = dados_doacao['motivo']
        if (doador and cachorro):
            doacao = Doacao(dados_doacao["data"], cachorro, doador, motivo)
            self.__doacoes.append(doacao)
            self.__tela_doacao.mostra_mensagem("Doacao realizada com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Dados invalidos")

    def listar_doacoes(self):
        if len(self.__doacoes) == 0:
            self.__tela_doacao.mostra_mensagem("Nenhuma doacao cadastrada")
        for doacao in self.__doacoes:
            self.__tela_doacao.mostra_doacao(doacao)
    
    def listar_doacoes_por_periodo(self):
        if len(self.__doacoes) == 0:
            self.__tela_doacao.mostra_mensagem("Nenhuma doacao cadastrada")
        else:
            data_inicio = self.__tela_doacao.pega_data('Data de inicio (DD/MM/AAAA): ')
            data_fim = self.__tela_doacao.pega_data('Data de fim (DD/MM/AAAA): ')
            for doacao in self.__doacoes:
                if doacao.date >= data_inicio and doacao.date <= data_fim:
                    self.__tela_doacao.mostra_doacao(doacao)

    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao_cachorro,
            2: self.incluir_doacao_gato,
            3: self.listar_doacoes,
            4: self.listar_doacoes_por_periodo,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            