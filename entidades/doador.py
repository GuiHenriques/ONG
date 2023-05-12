from entidades.pessoa import Pessoa
from datetime import date as Date


class Doador(Pessoa):


    def __init__(self,nome: str, cpf: str, data_nascimento: Date, endereco: str):
        super().__init__(nome, cpf, data_nascimento, endereco)

    