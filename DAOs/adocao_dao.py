from DAOs.DAO import DAO
from entidades.adocao import Adocao
from entidades.adotante import Adotante


class AdocaoDAO(DAO):
    def __init__(self):
        super().__init__('adocoes.pkl')

    def add(self, adocao):
        if ((adocao is not None) and isinstance(adocao,Adocao)):
            super().add(adocao.adotante.cpf, adocao)

    def update(self, adocao):
        if ((adocao is not None) and isinstance(adocao,Adocao)):
            super().update(adocao.adotante.cpf, adocao)

    def get(self,key):
        if isinstance(key,str):
            return super().get(key)

    def remove(self,key):
        if isinstance(key,str):
            return super().remove(key)