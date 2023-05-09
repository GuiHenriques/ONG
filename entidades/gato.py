from animal import Animal
from adocao import Adocao

class Gato(Animal):
    def __init__(self, chip: int, nome: str, raca: str, vacinas: list, adocao_atual : Adocao, tamanho: str):
        super().__init__(chip,nome,raca,vacinas,adocao_atual)