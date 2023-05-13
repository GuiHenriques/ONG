from entidades.gato import Gato
from telas.tela_gato import TelaGato

class ControladorGato:
    
    def __init__(self, controlador_sistema):
        self.__gatos = []
        self.__tela_gato = TelaGato()
        self.__controlador_sistema = controlador_sistema
    
    def inclui_gato(self):
        dados_gato = self.__tela_gato.pega_dados_gato()
        gato = Gato(dados_gato["nome"], dados_gato["raca"], dados_gato["idade"])
        self.__gatos.append(gato)
    
    def altera_gato(self):
        self.lista_gatos()
        chip = self.__tela_gato.seleciona_gato()
        gato = self.pega_gato_por_chip(chip)

        if gato:
            novos_dados_gato = self.__tela_gato.pega_dados_gato()
            gato.nome = novos_dados_gato["nome"]
            gato.raca = novos_dados_gato["raca"]
            gato.idade = novos_dados_gato["idade"]
            print("Gato alterado com sucesso")
        else:
            print("Gato não encontrado")
    
    def lista_gatos(self):
        if len(self.__gatos) == 0:
            print("Não há gatos cadastrados")
        else:
            for gato in self.__gatos:
                self.__tela_gato.mostra_gato(gato)
    
    def exclui_gato(self):
        self.lista_gatos()
        chip = self.__tela_gato.seleciona_animal()
        gato = self.pega_gato_por_chip(chip)

        if gato:
            self.__gatos.remove(gato)
            print("Gato excluído com sucesso")
        else:
            print("Gato não encontrado")
    
    def pega_gato_por_chip(self, chip):
        for gato in self.__gatos:
            if gato.chip == chip:
                return gato
        return None

    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_gato,
                        2: self.altera_gato,
                        3: self.lista_gatos,
                        4: self.exclui_gato,
                        0: self.retorna}

        while True:
            opcao_escolhida = self.__tela_gato.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            