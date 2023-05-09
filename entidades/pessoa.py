from abc import ABC, abstractmethod
from datetime import date as Date
#nao entendi o que o tipo significa, talvez doador/adotante? nao sei, pretendo apagar.
class Pessoa(ABC):
    @abstractmethod
    def __init__(self, cpf: str, nome: str, data_nascimento: Date,
                 endereco: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__endereco = endereco
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
