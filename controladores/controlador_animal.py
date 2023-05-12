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
        self.lista_cachorros()
        chip = self.__tela_animal.seleciona_animal()
        cachorro = self.pega_cachorro_por_chip(chip)

        if cachorro:
            novos_dados_cachorro = self.__tela_animal.pega_dados_cachorro()
            cachorro.nome = novos_dados_cachorro["nome"]
            cachorro.raca = novos_dados_cachorro["raca"]
            cachorro.idade = novos_dados_cachorro["idade"]
            cachorro.tamanho = novos_dados_cachorro["tamanho"]
            print("Cachorro alterado com sucesso")
        else:
            print("Cachorro não encontrado")
    
    def altera_gato(self):
        self.lista_gatos()
        chip = self.__tela_animal.seleciona_animal()
        gato = self.pega_gato_por_chip(chip)

        if gato:
            novos_dados_gato = self.__tela_animal.pega_dados_gato()
            gato.nome = novos_dados_gato["nome"]
            gato.raca = novos_dados_gato["raca"]
            gato.idade = novos_dados_gato["idade"]
            print("Gato alterado com sucesso")
        else:
            print("Gato não encontrado")

    
    def lista_cachorros(self):
        if len(self.__cachorros) == 0:
            print("Não há cachorros cadastrados")
        else:
            for cachorro in self.__cachorros:
                self.__tela_animal.mostra_cachorro(cachorro)
    
    def lista_gatos(self):
        if len(self.__gatos) == 0:
            print("Não há gatos cadastrados")
        else:
            for gato in self.__gatos:
                self.__tela_animal.mostra_gato(gato)
    
    def exclui_cachorro(self):
        self.lista_cachorros()
        chip = self.__tela_animal.seleciona_animal()
        cachorro = self.pega_cachorro_por_chip(chip)

        if cachorro:
            self.__cachorros.remove(cachorro)
            print("Cachorro excluído com sucesso")
        else:
            print("Cachorro não encontrado")
    
    def exclui_gato(self):
        self.lista_gatos()
        chip = self.__tela_animal.seleciona_animal()
        gato = self.pega_gato_por_chip(chip)

        if gato:
            self.__gatos.remove(gato)
            print("Gato excluído com sucesso")
        else:
            print("Gato não encontrado")
    
    def pega_cachorro_por_chip(self, chip):
        for cachorro in self.__cachorros:
            if cachorro.chip == chip:
                return cachorro
        return None

    def pega_gato_por_chip(self, chip):
        for gato in self.__gatos:
            if gato.chip == chip:
                return gato
        return None
    
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
            