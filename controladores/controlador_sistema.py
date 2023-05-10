from telas.tela_sistema import TelaSistema
from controlador_pessoa import ControladorPessoa
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
        
    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_livros, 2: self.cadastra_amigos, 3: self.cadastra_emprestimos,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
            
ControladorSistema().inicializa_sistema()