from entidades.adocao import Adocao
from telas.tela_adocao import TelaAdocao


class ControladorAdocao():
    def __init__(self, controlador_sistema):
        self.__adocoes = list()
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    def incluir_adocao_gato(self):
        lista_adotantes = self.__controlador_sistema.controlador_pessoa.lista_adotantes()
        lista_gatos = self.__controlador_sistema.controlador_gato.lista_gatos()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        adotante = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_adocao["cpf"])
        print(adotante.nome)
        gato = self.__controlador_sistema.controlador_gato.pega_gato_por_chip(dados_adocao["chip"])
        print(gato.nome)
        self.__controlador_sistema.controlador_gato.mostra_gato(gato)

        if (adotante and gato):
            adocao = Adocao(dados_adocao["data"], gato, adotante)
            self.__adocoes.append(adocao)
            self.__tela_adocao.mostra_mensagem("Adocao realizada com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Dados invalidos")
    
    def incluir_adocao_cachorro(self):
        lista_adotantes = self.__controlador_sistema.controlador_pessoa.lista_adotantes()
        lista_cachorros = self.__controlador_sistema.controlador_cachorro.lista_cachorros()
        if lista_adotantes == None:
            self.__tela_adocao.mostra_mensagem('Não há adotantes registrados no sistema! ')
            self.retornar()
        if lista_cachorros == None:
            self.__tela_adocao.mostra_mensagem('Não há cachorros registrados no sistema! ')
            self.retornar()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        adotante = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_adocao["cpf"])
        cachorro = self.__controlador_sistema.controlador_cachorro.pega_cachorro_por_chip(dados_adocao["chip"])
        
        if (adotante and cachorro):
            adocao = Adocao(dados_adocao["data"], cachorro, adotante)
            self.__adocoes.append(adocao)
            self.__tela_adocao.mostra_mensagem("Adocao realizada com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Dados invalidos")

    def listar_adocoes(self):
        if len(self.__adocoes) == 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada")
        for adocao in self.__adocoes:
            self.__tela_adocao.mostra_adocao(adocao)
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao_cachorro,
            2: self.incluir_adocao_gato,
            3: self.listar_adocoes,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.__tela_adocao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            