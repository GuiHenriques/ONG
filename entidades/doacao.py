from entidades.doador import Doador
from datetime import date as Date
from entidades.animal import Animal

class Doacao():
    def __init__(self, date: Date, animal: Animal, doador: Doador, motivo: str):
        self.__date = date
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo
        
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
    def doador(self):
        return self.__doador
    
    @doador.setter
    def doador(self, doador):
        self.__doador = doador
    
    @property
    def motivo(self):
        return self.__motivo
    
    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo

    
    