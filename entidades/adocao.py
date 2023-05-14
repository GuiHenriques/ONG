from entidades.adotante import Adotante
from entidades.animal import Animal
from datetime import date as Date

class Adocao():
    def __init__(self, data: Date, animal: Animal, adotante: Adotante):
        self.__data = data
        self.__animal = animal
        self.__adotante = adotante
        self.__termo_responsa = False
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal):
        self.__animal = animal
        
    @property
    def adotante(self):
        return self.__adotante
    
    @adotante.setter
    def adotante(self, adotante):
        self.__adotante = adotante
        
    @property
    def termo_responsa(self):
        return self.__termo_responsa
    
    @termo_responsa.setter
    def termo_responsa(self, termo_responsa):
        self.__termo_responsa = termo_responsa
        
    #relatorio