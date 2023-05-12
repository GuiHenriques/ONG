from telas.tela_pessoa import TelaPessoa
import controladores.controlador_sistema as ControladorSistema

class ControladorPessoa:

    def __init__(self, controlador_sistema: ControladorSistema):
        self.__adotantes = list()
        self.__doadores = list()
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema
    
    def incluir_adotante(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_adotante()