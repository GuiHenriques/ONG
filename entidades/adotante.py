from entidades.pessoa import Pessoa
from datetime import date as Date


class Adotante(Pessoa):

    def __init__(self,nome: str, cpf: str, data_nascimento: Date, endereco: str, tipo_hab : str, tam_hab: str, outros_animais: str):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.__tipo_hab = tipo_hab
        self.__tam_hab = tam_hab
        self.__outros_animais = outros_animais

    @property
    def tipo_hab(self):
        return self.__tipo_hab

    @tipo_hab.setter
    def tipo_hab(self, tipo_hab):
        self.__tipo_hab = tipo_hab

    @property
    def tam_hab(self):
        return self.__tam_hab

    @tam_hab.setter
    def tam_hab(self, tam_hab):
        self.__tam_hab = tam_hab

    @property
    def outros_animais(self):
        return self.__outros_animais

    @outros_animais.setter
    def outros_animais(self, outros_animais):
        self.__outros_animais = outros_animais
