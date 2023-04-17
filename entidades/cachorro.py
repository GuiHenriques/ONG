from animal import Animal

class Cachorro(Animal):
    def __init__(self, chip, nome,  raca, tamanho):
        super().__init__(chip, nome, raca)
        self.__tamanho = tamanho

    # tamanho
    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho
