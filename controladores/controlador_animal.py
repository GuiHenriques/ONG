from telas.tela_animal import TelaAnimal
from entidades.cachorro import Cachorro
from entidades.gato import Gato

    
class ControladorAnimal:

    def __init__(self, controlador_sistema):
        self.__cachorros = []
        self.__gatos = []
        self.__tela_animal = TelaAnimal()
        self.__controlador_sistema = controlador_sistema

    def inclui_cachorro(self):
        dados_cachorro = self.__tela_animal.pega_dados_cachorro()
        cachorro = Cachorro(dados_cachorro["nome"], dados_cachorro["raca"], dados_cachorro["idade"], dados_cachorro["tamanho"])
        self.__cachorros.append(cachorro)

    def inclui_gato(self):
        dados_gato = self.__tela_animal.pega_dados_gato()
        gato = Gato(dados_gato["nome"], dados_gato["raca"], dados_gato["idade"])
        self.__gatos.append(gato)
    
    def altera_cachorro(self):
        ...
    
    def altera_gato(self):
        ...
    
    def lista_cachorros(self):
        for cachorro in self.__cachorros:
            self.__tela_animal.mostra_cachorro({"nome": cachorro.nome, "raca": cachorro.raca, "idade": cachorro.idade, "tamanho": cachorro.tamanho})
    
    def lista_gatos(self):
        for gato in self.__gatos:
            self.__tela_animal.mostra_gato({"nome": gato.nome, "raca": gato.raca, "idade": gato.idade})
    
    def exclui_cachorro(self):
        ...
    
    def exclui_gato(self):
        ...
    
    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cachorro,
                        2: self.altera_cachorro,
                        3: self.lista_cachorros,
                        4: self.exclui_cachorro,
                        5: self.inclui_gato,
                        6: self.altera_gato,
                        7: self.lista_gatos,
                        8: self.exclui_gato,
                        0: self.retorna}

        while True:
            opcao_escolhida = self.__tela_animal.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            