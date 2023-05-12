from telas.tela_animal import TelaAnimal
from entidades.animal import Animal

    
class ControladorAnimal:

    def __init__(self, controlador_sistema):
        self.__animais = []
        self.__tela_animal = TelaAnimal()
        self.__controlador_sistema = controlador_sistema

    def inclui_animal(self):
        ...

    def altera_animal(self):
        ...
    
    def lista_animais(self):
        ...
    
    def exclui_animal(self):
        ...
    
    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_animal,
                        2: self.altera_animal,
                        3: self.lista_animais,
                        4: self.exclui_animal,
                        0: self.retorna}

        while True:
            opcao_escolhida = self.__tela_animal.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            