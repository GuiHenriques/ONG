from entidades.animal import Animal

class Gato(Animal):
    def __init__(self, nome: str, raca: str):
        super().__init__(nome,raca)