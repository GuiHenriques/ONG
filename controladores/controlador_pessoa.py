from telas.tela_pessoa import TelaPessoa
from entidades.adotante import Adotante

class ControladorPessoa():

    def __init__(self, controlador_sistema):
        self.__adotantes = list()
        self.__doadores = list()
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    def incluir_adotante(self):
        dados_adotante = self.__tela_pessoa.pega_dados_adotante()
        adotante = Adotante(dados_adotante['nome'], dados_adotante['cpf'], dados_adotante['data_nascimento'],
                            dados_adotante['endereco'], dados_adotante['tipo_hab'], dados_adotante['tam_hab'], dados_adotante['outros_animais'])
        self.__adotantes.append(adotante)
        self.__tela_pessoa.mostra_mensagem('Adotante incluído com sucesso! ')

    def pega_pessoa_por_cpf(self, cpf: str):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None
    def altera_adotante(self):
        self.lista_adotante()
        cpf_adotante = self.__tela_pessoa.pega_cpf()
        adotante = self.pega_pessoa_por_cpf(cpf_adotante) #serve para garantir que a pessoa esta na lista

        if adotante != None:
        #if cpf(is not None):
            novos_dados_adotante = self.__tela_pessoa.pega_dados_adotante()
            adotante.nome = novos_dados_adotante['nome']
            adotante.cpf = novos_dados_adotante['cpf']
            adotante.data_nascimento = novos_dados_adotante['data_nascimento']
            adotante.endereco = novos_dados_adotante['endereco']
            adotante.tipo_hab = novos_dados_adotante['tipo_hab']
            adotante.tam_hab = novos_dados_adotante['tam_hab']
            adotante.outros_animais = novos_dados_adotante['outros_animais']
            self.__tela_pessoa.mostra_mensagem('Dados do adotante alterado!')
            self.lista_adotante()



    def lista_adotante(self):
        for adotante in self.__adotantes:
            self.__tela_pessoa.mostra_adotante({'nome': adotante.nome, 'cpf': adotante.cpf, 'data_nascimento': adotante.data_nascimento,
                                                'endereco': adotante.endereco,'tipo_hab': adotante.tipo_hab, 'tam_hab': adotante.tam_hab, 'outros_animais': adotante.outros_animais})

    def excluir_adotante(self):
        self.lista_adotante()
        cpf = self.__tela_pessoa.pega_cpf()
        adotante = self.pega_pessoa_por_cpf(cpf)
        if adotante != None:
            self.__adotantes.remove(adotante)
            self.__tela_pessoa.mostra_mensagem('Adotante removido!')
            self.lista_adotante()

    def incluir_doador(self):
        pass

    def altera_doador(self):
        pass

    def lista_doador(self):
        pass

    def excluir_doador(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()


    def abre_tela(self):
        lista_opcoes = {1: self.incluir_adotante, 2: self.altera_adotante, 3: self.lista_adotante, 4: self.excluir_adotante,
                        5: self.incluir_doador, 6: self.altera_doador, 7: self.lista_doador, 8: self.excluir_doador,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()