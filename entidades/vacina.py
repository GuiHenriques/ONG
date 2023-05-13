from entidades.animal import Animal
from datetime import date as Date


class Vacina():
    def __init__(self, date: Date, animal: Animal, tipo: str):
        self.__date = date
        self.__animal = animal
        self.__tipo = tipo
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date
    
    @property
    def animal(self):
        return self.__animal
    
    @animal.setter
    def animal(self, animal):
        self.__animal = animal
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    