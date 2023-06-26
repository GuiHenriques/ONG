from DAOs.DAO import DAO
from entidades.cachorro import Cachorro
from entidades.gato import Gato

class AnimalDAO(DAO):
    def __init__(self):
        super().__init__('animais.pkl')

    def add(self, animal):
        if ((animal is not None) and isinstance(animal.chip, int)) and (isinstance(animal, Cachorro) or isinstance(animal, Gato)):
            super().add(animal.chip, animal)

    def update(self, animal):
        if ((animal is not None) and isinstance(animal.chip, int)) and (isinstance(animal, Cachorro) or isinstance(animal, Gato)):
            super().update(animal.chip, animal)

    def get(self,key):
        if isinstance(key,int):
            return super().get(key)

    def remove(self,chip):
        if isinstance(chip,int):
            return super().remove(chip)