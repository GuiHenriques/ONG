from entidades.adocao import Adocao
from telas.tela_adocao import TelaAdocao


class ControladorAdocao():
    def __init__(self, controlador_sistema):
        self.__adocoes = list()
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    def incluir_adocao_gato(self):
        ...
    
    def incluir_adocao_cachorro(self):
        ...

    def listar_adocoes(self):
        if len(self.__adocoes) == 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada")
        for adocao in self.__adocoes:
            self.__tela_adocao.mostra_adocao(adocao)
    
    def listar_adocoes_por_periodo(self):
        if len(self.__adocoes) == 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada")
        else:
            data_inicial = self.__tela_adocao.pega_data("Data inicial (DD/MM/AAAA): ")
            data_final = self.__tela_adocao.pega_data("Data final (DD/MM/AAAA): ")
            for adocao in self.__adocoes:
                if adocao.data >= data_inicial and adocao.data <= data_final:
                    self.__tela_adocao.mostra_adocao(adocao)
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao_cachorro,
            2: self.incluir_adocao_gato,
            3: self.listar_adocoes,
            4: self.listar_adocoes_por_periodo,
            0: self.retornar
        }


        while True:
            opcao_escolhida = self.__tela_adocao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            