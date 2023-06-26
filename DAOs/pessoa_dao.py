from DAOs.DAO import DAO
from entidades.adotante import Adotante
from entidades.doador import Doador

#cada entidade terá uma classe dessa, implementação bem simples.
class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoas.pkl')

    def add(self, pessoa):
        if (pessoa) and isinstance(pessoa, Adotante) or isinstance(pessoa, Doador):
            super().add(pessoa.cpf, pessoa)
    
    def update(self, pessoa):
        if (pessoa) and isinstance(pessoa, Adotante) or isinstance(pessoa, Doador):
            super().update(pessoa.cpf, pessoa)
    
    def get(self, key):
        if isinstance(key, str):
            return super().get(key)
    
    def remove(self, key):
        if isinstance(key, str):
            return super().remove(key)
        