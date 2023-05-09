from animal import Animal
from adocao import Adocao

class Cachorro(Animal):
    def __init__(self, chip: int, nome: str, raca: str, vacinas: list, adocao_atual : Adocao, tamanho: str):
        super().__init__(chip,nome,raca,vacinas,adocao_atual)
        self.__tamanho = tamanho
        
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho
        