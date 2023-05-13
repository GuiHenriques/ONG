from entidades.cachorro import Cachorro
from telas.tela_cachorro import TelaCachorro


class ControladorCachorro:

    def __init__(self, controlador_sistema):
        self.__cachorros = []
        self.__tela_cachorro = TelaCachorro()
        self.__controlador_sistema = controlador_sistema
    
    def inclui_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        cachorro = Cachorro(dados_cachorro["nome"], dados_cachorro["raca"], dados_cachorro["idade"], dados_cachorro["tamanho"])
        self.__cachorros.append(cachorro)
    
    def altera_cachorro(self):
        self.lista_cachorros()
        chip = self.__tela_cachorro.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_chip(chip)

        if cachorro:
            novos_dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
            cachorro.nome = novos_dados_cachorro["nome"]
            cachorro.raca = novos_dados_cachorro["raca"]
            cachorro.idade = novos_dados_cachorro["idade"]
            cachorro.tamanho = novos_dados_cachorro["tamanho"]
            print("Cachorro alterado com sucesso")
        else:
            print("Cachorro não encontrado")
    
    def lista_cachorros(self):
        if len(self.__cachorros) == 0:
            print("Não há cachorros cadastrados")
        else:
            for cachorro in self.__cachorros:
                self.__tela_cachorro.mostra_cachorro(cachorro)
    
    def exclui_cachorro(self):
        self.lista_cachorros()
        chip = self.__tela_cachorro.seleciona_animal()
        cachorro = self.pega_cachorro_por_chip(chip)

        if cachorro:
            self.__cachorros.remove(cachorro)
            print("Cachorro excluído com sucesso")
        else:
            print("Cachorro não encontrado")
        
    def pega_cachorro_por_chip(self, chip):
        for cachorro in self.__cachorros:
            if cachorro.chip == chip:
                return cachorro
        return None

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cachorro,
                        2: self.altera_cachorro,
                        3: self.lista_cachorros,
                        4: self.exclui_cachorro,
                        0: self.retorna}

        while True:
            opcao_escolhida = self.__tela_cachorro.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            