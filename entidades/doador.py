from pessoa import Pessoa
from datetime import date as Date

class Doador(Pessoa):
    def __init__(self,cpf: str, nome: str, data_nascimento: Date, endereco: str):
        super().__init__(cpf,nome,data_nascimento,endereco)
    