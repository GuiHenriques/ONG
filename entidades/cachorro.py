from entidades.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, tamanho: str):
        super().__init__(nome,raca)
        self.__tamanho = tamanho
        
    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho
        