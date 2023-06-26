from entidades.animal import Animal

class Gato(Animal):
    def __init__(self, chip:int, nome: str, raca: str, idade: int):
        super().__init__(chip, nome, raca, idade)