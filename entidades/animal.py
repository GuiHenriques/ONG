from abc import ABC, abstractmethod
import pickle
class Animal(ABC):

    #numero_chip = 1

    @abstractmethod
    def __init__(self, chip: int,nome: str, raca: str, idade: int):
        self.__chip = chip
        #Animal.numero_chip += 1
        #arq_numero_chip = ('numero.pkl','wb')
        #pickle.dump(Animal.numero_chip, arq_numero_chip)
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade
        self.__vacinas = []
        self.__disponivel = False
    
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
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def vacinas(self):
        return self.__vacinas

    @vacinas.setter
    def adocao_atual(self, vacinas):
        self.__vacinas = vacinas

    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel
