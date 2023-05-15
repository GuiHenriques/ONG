from entidades.gato import Gato
from entidades.vacina import Vacina
from telas.tela_gato import TelaGato

class ControladorGato:
    
    def __init__(self, controlador_sistema):
        self.__gatos = []
        self.__tela_gato = TelaGato()
        self.__controlador_sistema = controlador_sistema
    
    def inclui_gato(self):
        dados_gato = self.__tela_gato.pega_dados_gato()
        gato = Gato(dados_gato["nome"], dados_gato["raca"], dados_gato["idade"])
        self.__gatos.append(gato)
        self.__tela_gato.mostra_mensagem("Gato cadastrado com sucesso")
    
    def altera_gato(self):
        self.lista_gatos()
        try:
            chip = int(self.__tela_gato.seleciona_gato())
        except ValueError:
            self.__tela_gato.mostra_mensagem("Chip Inválido")
        gato = self.pega_gato_por_chip(chip)

        if gato:
            novos_dados_gato = self.__tela_gato.pega_dados_gato()
            gato.nome = novos_dados_gato["nome"]
            gato.raca = novos_dados_gato["raca"]
            gato.idade = novos_dados_gato["idade"]
            self.__tela_gato.mostra_mensagem("Gato alterado com sucesso")
        else:
            self.__tela_gato.mostra_mensagem("Gato não encontrado")
    
    def lista_gatos(self):
        if len(self.__gatos) == 0:
            self.__tela_gato.mostra_mensagem("Não há gatos cadastrados")
        else:
            for gato in self.__gatos:
                self.__tela_gato.mostra_gato(gato)
    
    def lista_gatos_disponiveis(self):
        if len(self.__gatos) == 0:
            self.__tela_gato.mostra_mensagem("Não há gatos cadastrados")
        else:
            for gato in self.__gatos:
                if gato.disponivel:
                    self.__tela_gato.mostra_gato(gato)
    
    def exclui_gato(self):
        self.lista_gatos()
        try:
            chip = int(self.__tela_gato.seleciona_gato())
        except ValueError:
            self.__tela_gato.mostra_mensagem("Chip Inválido")
        gato = self.pega_gato_por_chip(chip)

        if gato:
            self.__gatos.remove(gato)
            self.__tela_gato.mostra_mensagem("Gato excluído com sucesso")
        else:
            self.__tela_gato.mostra_mensagem("Gato não encontrado")
    
    def adicionar_vacina(self):
        self.lista_gatos()
        try:
            chip = int(self.__tela_gato.seleciona_gato())
        except ValueError:
            self.__tela_gato.mostra_mensagem("Chip Inválido")
        gato = self.pega_gato_por_chip(chip)

        if gato:
            dados_vacina = self.__tela_gato.pega_dados_vacina()
            vacina = Vacina(dados_vacina["data"], gato, dados_vacina["tipo"])
            gato.vacinas.append(vacina)
            if len(gato.vacinas) == 3:
                gato.disponivel = True
            self.__tela_gato.mostra_mensagem("Vacina adicionada com sucesso")
        else:
            self.__tela_gato.mostra_mensagem("Gato não encontrado")
    
    def pega_gato_por_chip(self, chip):
        for gato in self.__gatos:
            if gato.chip == chip:
                return gato
        return None

    def retorna(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_gato,
                        2: self.altera_gato,
                        3: self.lista_gatos,
                        4: self.exclui_gato,
                        5: self.adicionar_vacina,
                        0: self.retorna}

        while True:
            opcao_escolhida = self.__tela_gato.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            