from entidades.animal import Animal

class Cachorro(Animal):
    def __init__(self, chip:int,nome: str, raca: str, idade: int, tamanho: str):
        super().__init__(chip, nome,raca,idade)
        self.__tamanho = tamanho
        
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho