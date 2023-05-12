from animal import Animal
from adocao import Adocao

class Gato(Animal):
    def __init__(self, chip: int, nome: str, raca: str, idade: int, vacinas: list, disponivel : bool):
        super().__init__(chip,nome,raca,vacinas,disponivel)