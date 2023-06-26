from DAOs.DAO import DAO
from entidades.doacao import Doacao
from entidades.doador import Doador


class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__('doacoes.pkl')

    def add(self, doacao):
        if ((doacao is not None) and isinstance(doacao,Doacao)):
            super().add(doacao.doador.cpf, doacao)

    def update(self, doacao):
        if ((doacao is not None) and isinstance(doacao,Doacao)):
            super().update(doacao.doador.cpf, doacao)

    def get(self,key):
        if isinstance(key,str):
            return super().get(key)

    def remove(self,key):
        if isinstance(key,str):
            return super().remove(key)