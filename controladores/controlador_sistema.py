from telas.tela_sistema import TelaSistema
from controladores.controlador_pessoa import ControladorPessoa
from controlador_doacao import ControladorDoacao
from controlador_adocao import ControladorAdocao


class ControladorSistema():
    
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    # não tem controlador emprestimo na exemplo mvc
    @property
    def controlador_adocao(self):
        return self.__controlador_adocao
    
    @property
    def controlador_doacao(self):
        return self.__controlador_doacao
    
    def inicializa_sistema(self):
        self.abre_tela()
    

    def controle_pessoa(self):
        ...
    
    def controle_animal(self):
        self.__controlador_animal.abre_tela()
        
    def controle_adocao(self):
        self.__controlador_adocao.abre_tela()

    def controle_doacao(self):
        ...

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.controle_animal,
            2: self.controle_pessoa,
            3: self.controle_adocao,
            4: self.controle_doacao,
            0: self.encerra_sistema,
        }
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            lista_opcoes[opcao]()

        
    def abre_tela(self):
        lista_opcoes = {1: self.controle_animal, 2: self.controle_pessoa, 3: self.controle_adocao, 4: self.controle_doacao,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
            
ControladorSistema().inicializa_sistema()