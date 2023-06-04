from telas.tela_pessoa import TelaPessoa
from entidades.adotante import Adotante
from entidades.doador import Doador


class ControladorPessoa:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()
        self.__pessoas = []
        self.__tipo = None
    
    @property
    def tela_pessoa(self):
        return self.__tela_pessoa

    @property
    def pessoas(self):
        return self.__pessoas

    def incluir_pessoa(self):
        dados_pessoa = self.tela_pessoa.pega_dados_pessoa(self.tipo)

        if self.tipo == "Adotante":
            pessoa = Adotante(
                dados_pessoa["nome"],
                dados_pessoa["cpf"],
                dados_pessoa["data_nascimento"],
                dados_pessoa["endereco"],
                dados_pessoa["tipo_hab"],
                dados_pessoa["tam_hab"],
                dados_pessoa["outros_animais"],
            )
        else:
            pessoa = Doador(
                dados_pessoa["nome"],
                dados_pessoa["cpf"],
                dados_pessoa["data_nascimento"],
                dados_pessoa["endereco"],
            )
        
        # CPF repetido

        self.pessoas.append(pessoa)
        self.tela_pessoa.mostra_mensagem(f"{self.tipo} incluído com sucesso!")
        animal = self.tela_pessoa.seleciona_animal()
        self.__controlador_sistema.controlador_animal.tipo = animal
        animal = self.__controlador_sistema.controlador_animal.inclui_animal()
        self.__controlador_sistema.controlador_doacao.inclui_doacao(animal, pessoa)

    

    def altera_pessoa(self):
        if not self.lista_pessoas():
            return
        cpf = self.tela_pessoa.seleciona_pessoa_por_cpf()
        pessoa = self.pega_pessoa_por_cpf(cpf)

        if pessoa:
            novos_dados_pessoa = self.tela_pessoa.pega_dados_pessoa(self.tipo)
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.cpf = novos_dados_pessoa["cpf"]
            pessoa.data_nascimento = novos_dados_pessoa["data_nascimento"]
            pessoa.endereco = novos_dados_pessoa["endereco"]
            
            if self.tipo == "Adotante":
                pessoa.tipo_hab = novos_dados_pessoa["tipo_hab"]
                pessoa.tam_hab = novos_dados_pessoa["tam_hab"]
                pessoa.outros_animais = novos_dados_pessoa["outros_animais"]
            
            self.tela_pessoa.mostra_mensagem(f"Dados do {self.tipo} alterado!")
        
        else:
            self.tela_pessoa.mostra_mensagem("CPF não cadastrado!")
            

    def lista_pessoas(self):
        condicao = lambda pessoa: isinstance(pessoa, Adotante) if self.tipo == "Adotante" else isinstance(pessoa, Doador)
        
        if len([pessoa for pessoa in self.pessoas if condicao(pessoa)]) == 0:
            self.tela_pessoa.mostra_mensagem(f"Não tem {self.tipo} cadastrado!")
            return None

        for pessoa in self.pessoas:
            dados_pessoa = {
                "nome": pessoa.nome, 
                "cpf": pessoa.cpf,
                "data_nascimento": pessoa.data_nascimento,
                "endereco": pessoa.endereco,
            }
            
            if self.tipo == "Adotante" and isinstance(pessoa, Adotante):
                dados_pessoa["tipo_hab"] = pessoa.tipo_hab
                dados_pessoa["tam_hab"] = pessoa.tam_hab
                dados_pessoa["outros_animais"] = pessoa.outros_animais
        
            self.tela_pessoa.mostra_pessoa(dados_pessoa)

    def excluir_pessoa(self):
        if not self.lista_pessoas():
            return
        cpf = self.tela_pessoa.seleciona_pessoa_por_cpf()
        pessoa = self.pega_pessoa_por_cpf(cpf)
        
        if pessoa:
            self.pessoas.remove(pessoa)
            self.tela_pessoa.mostra_mensagem(f"{self.tipo} removido!")
        else:
            self.tela_pessoa.mostra_mensagem("CPF não cadastrado!")


    def pega_pessoa_por_cpf(self, cpf: str):
        for pessoa in self.pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def tipo_pessoa(self):
        self.tipo = self.tela_pessoa.seleciona_tipo_pessoa()
        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pessoa,
            2: self.altera_pessoa,
            3: self.lista_pessoas,
            4: self.excluir_pessoa,
            0: self.retornar,
        }

        while True:
            lista_opcoes[self.tela_pessoa.tela_opcoes(self.tipo)]()
