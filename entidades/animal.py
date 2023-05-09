from adocao import Adocao

class Animal():
    def __init__(self, chip: int, nome: str, raca: str, vacinas: list, adocao_atual: Adocao):
        self.__chip = chip
        self.__nome = nome
        self.__raca = raca
        self.__vacinas = vacinas
        self.__adocao_atual = adocao_atual
    
    @property
    def chip(self):
        return self.__chip
    
    @chip.setter
    def chip(self, chip):
        self.__chip = chip
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, raca):
        self.__raca = raca
        
    @property
    def vacinas(self):
        return self.__vacinas
    
    #fazer setter de vacinas?
    @property
    def adocao_atual(self):
        return self.__adocao_atual