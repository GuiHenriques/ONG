class ControladorDoacao():


    def __init__(self, controlador_sistema):
        self.__doacoes = list()
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema