from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao

class ControladorDoacao():

    def __init__(self, controlador_sistema):
        self.__doacoes = list()
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema

    @property
    def doacoes(self):
        return self.__doacoes
    
    def incluir_doacao(self, animal, pessoa):
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        doacao = Doacao(dados_doacao["data"], animal, pessoa, dados_doacao["motivo"])
        self.doacoes.append(doacao)
        self.__tela_doacao.mostra_mensagem("Adocao realizada com sucesso!")
    
    def listar_doacoes(self):
        if len(self.doacoes) == 0:
            self.__tela_doacao.mostra_mensagem("Nenhuma doacao cadastrada")
        for doacao in self.doacoes:
            dados_doacao = {"data": doacao.data, }
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
            