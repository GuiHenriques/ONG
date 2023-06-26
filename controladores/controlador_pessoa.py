from telas.tela_pessoa import TelaPessoa
from entidades.adotante import Adotante
from entidades.doador import Doador
from DAOs.pessoa_dao import PessoaDAO


class ControladorPessoa:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()
        # self.__pessoas = [Adotante("João", "12345678910", "01/01/2000", "Rua A", "Casa", "Pequeno", "Sim"),Doador("Maria", "10987654321", "01/01/2000", "Rua B")]
        self.__pessoa_dao = PessoaDAO()
        self.__tipo = None

    @property
    def tela_pessoa(self):
        return self.__tela_pessoa

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def pessoas(self):
        return self.__pessoas

    def inclui_pessoa(self):
        dados_pessoa = self.tela_pessoa.pega_dados_pessoa(self.tipo)
        if not dados_pessoa:
            return
        
        if self.tipo == "Adotante":
            pessoa = Adotante(
                dados_pessoa["nome"],
                dados_pessoa["cpf"],
                dados_pessoa["data"],
                dados_pessoa["endereco"],
                dados_pessoa["tipo_hab"],
                dados_pessoa["tam_hab"],
                dados_pessoa["outros_animais"]
            )
        else:
            pessoa = Doador(
                dados_pessoa["nome"],
                dados_pessoa["cpf"],
                dados_pessoa["data"],
                dados_pessoa["endereco"]
            )

        self.__pessoa_dao.add(pessoa)
        self.tela_pessoa.mostra_mensagem("Sucesso", f"{self.tipo} incluído com sucesso")

    def altera_pessoa(self):
        if not self.lista_pessoas():
            return
        cpf = self.tela_pessoa.pega_cpf()
        if not cpf: return
        
        pessoa = self.pega_pessoa_por_cpf(cpf)

        if pessoa:
            novos_dados_pessoa = self.tela_pessoa.pega_dados_pessoa(self.tipo)
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.cpf = novos_dados_pessoa["cpf"]
            pessoa.data_nascimento = novos_dados_pessoa["data"]
            pessoa.endereco = novos_dados_pessoa["endereco"]

            if self.tipo == "Adotante":
                pessoa.tipo_hab = novos_dados_pessoa["tipo_hab"]
                pessoa.tam_hab = novos_dados_pessoa["tam_hab"]
                pessoa.outros_animais = novos_dados_pessoa["outros_animais"]
    
            self.__pessoa_dao.update(pessoa)
            self.tela_pessoa.mostra_mensagem("Sucesso", f"Dados do {self.tipo} alterado!")
    
    def lista_pessoas(self):
        condicao = (
            lambda pessoa: isinstance(pessoa, Adotante)
            if self.tipo == "Adotante"
            else isinstance(pessoa, Doador)
        )

        if len([pessoa for pessoa in self.__pessoa_dao.get_all() if condicao(pessoa)]) == 0:
            self.tela_pessoa.mostra_mensagem("Erro", f"Nenhum {self.tipo} cadastrado")
            return

        lista_de_pessoas = []
        header = ( 
            ["Nome", "CPF", "Nascimento", "Endereço", "Habitação", "Tamanho Hab.", "Outros Animais"] if self.tipo == "Adotante"
              else ["Nome", "CPF", "Nascimento", "Endereço"]
        )
        lista_de_pessoas.append(header)

        for pessoa in self.__pessoa_dao.get_all():
            dados_pessoa = [pessoa.nome, pessoa.cpf, pessoa.data_nascimento, pessoa.endereco]

            if self.tipo == "Adotante" and isinstance(pessoa, Adotante):
                dados_extras = [pessoa.tipo_hab, pessoa.tam_hab, pessoa.outros_animais]
                for dado in dados_extras:
                    dados_pessoa.append(dado)
                lista_de_pessoas.append(dados_pessoa)

            elif self.tipo == "Doador" and isinstance(pessoa, Doador):
                lista_de_pessoas.append(dados_pessoa)

        self.tela_pessoa.mostra_pessoa(lista_de_pessoas)
        return True

    def exclui_pessoa(self):
        self.lista_pessoas()
        cpf = self.tela_pessoa.pega_cpf()
        pessoa = self.pega_pessoa_por_cpf(cpf)

        if pessoa:
            self.__pessoa_dao.remove(pessoa)
            self.tela_pessoa.mostra_mensagem("Sucesso", f"{self.tipo} removido!")

    def pega_pessoa_por_cpf(self, cpf: str):
        for pessoa in self.__pessoa_dao.get_all():
            if pessoa.cpf == cpf:
                return pessoa
        self.tela_pessoa.mostra_mensagem("Erro", "CPF não cadastrado!")
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def tipo_pessoa(self):
        self.tipo = self.tela_pessoa.seleciona_tipo_pessoa()
        
        if self.tipo is None:
            self.retornar()

        self.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_pessoa,
            2: self.altera_pessoa,
            3: self.lista_pessoas,
            4: self.exclui_pessoa,
            0: self.retornar,
        }


        while True:
            opcao = self.tela_pessoa.tela_opcoes(self.tipo)
            lista_opcoes[opcao]()