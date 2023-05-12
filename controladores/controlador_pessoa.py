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

    def altera_adotante(self):
        pass

    def lista_adotante(self):
        for adotante in self.__adotantes:
            self.__tela_pessoa.mostra_adotante({'nome': adotante.nome, 'cpf': adotante.cpf, 'data_nascimento': adotante.data_nascimento,
                                                'endereco': adotante.endereco,'tipo_hab': adotante.tipo_hab, 'tam_hab': adotante.tam_hab, 'outros_animais': adotante.outros_animais})

    def excluir_adotante(self):
        pass

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