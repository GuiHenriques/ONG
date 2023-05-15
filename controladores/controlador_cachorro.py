from entidades.vacina import Vacina
from entidades.cachorro import Cachorro
from telas.tela_cachorro import TelaCachorro

class ControladorCachorro:

    def __init__(self, controlador_sistema):
        self.__cachorros = [Cachorro("Dog1", "Pastor", 2, "G")]
        self.__cachorros[0].vacinas.append(
            Vacina("01/01/2020", self.__cachorros[0], "Raiva")
            )
        self.__cachorros[0].vacinas.append(
            Vacina("01/01/2020", self.__cachorros[0], "Leptospirose")
            )
        self.__cachorros[0].vacinas.append(
            Vacina("01/01/2020", self.__cachorros[0], "Hepatite Infecciosa")
            )
        self.__cachorros[0].disponivel = True
        self.__tela_cachorro = TelaCachorro()
        self.__controlador_sistema = controlador_sistema
    
    def inclui_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
        cachorro = Cachorro(dados_cachorro["nome"], dados_cachorro["raca"], dados_cachorro["idade"], dados_cachorro["tamanho"])
        self.__cachorros.append(cachorro)
        self.__tela_cachorro.mostra_mensagem("Cachorro cadastrado com sucesso")
    
    def altera_cachorro(self):
        self.lista_cachorros()
        try:
            chip = int(self.__tela_cachorro.seleciona_cachorro())
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("Chip Inválido")
            
        cachorro = self.pega_cachorro_por_chip(chip)

        if cachorro:
            novos_dados_cachorro = self.__tela_cachorro.pega_dados_cachorro()
            cachorro.nome = novos_dados_cachorro["nome"]
            cachorro.raca = novos_dados_cachorro["raca"]
            cachorro.idade = novos_dados_cachorro["idade"]
            cachorro.tamanho = novos_dados_cachorro["tamanho"]
            self.__tela_cachorro.mostra_mensagem("Cachorro alterado com sucesso")
        else:
            self.__tela_cachorro.mostra_mensagem("Cachorro não encontrado")
    
    def lista_cachorros(self):
        if len(self.__cachorros) == 0:
            self.__tela_cachorro.mostra_mensagem("Não há cachorros cadastrados")
        else:
            for cachorro in self.__cachorros:
                self.__tela_cachorro.mostra_cachorro(cachorro)
    
    def lista_cachorros_disponiveis(self):
        if len(self.__cachorros) == 0:
            self.__tela_cachorro.mostra_mensagem("Não há cachorros cadastrados")
            return None
        else:
            print("tem Cachorros disponíveis: ")
            for cachorro in self.__cachorros:
                if cachorro.disponivel:
                    self.__tela_cachorro.mostra_cachorro(cachorro)
            return True

    def exclui_cachorro(self):
        self.lista_cachorros()
        try:
            chip = int(self.__tela_cachorro.seleciona_cachorro())
        except ValueError:
            self.__tela_cachorro.mostra_mensagem("Chip Inválido")
            
        cachorro = self.pega_cachorro_por_chip(chip)

        if cachorro:
            self.__cachorros.remove(cachorro)
            self.__tela_cachorro.mostra_mensagem("Cachorro excluído com sucesso")
        else:
            self.__tela_cachorro.mostra_mensagem("Cachorro não encontrado")
    
    def adicionar_vacina(self):
        while True:
            try:
                self.lista_cachorros()
                chip = int(self.__tela_cachorro.seleciona_cachorro())
                cachorro = self.pega_cachorro_por_chip(chip)
                if cachorro == None:
                    raise ValueError
                break
            except ValueError:
                self.__tela_cachorro.mostra_mensagem("Chip Inválido")

        if cachorro:
            dados_vacina = self.__tela_cachorro.pega_dados_vacina()
            for vacina in cachorro.vacinas:
                if vacina.tipo == dados_vacina["tipo"]:
                    self.__tela_cachorro.mostra_mensagem("Vacina já aplicada")
                    self.abre_tela()
            vacina = Vacina(dados_vacina["data"], cachorro, dados_vacina["tipo"])
            cachorro.vacinas.append(vacina)
            if len(cachorro.vacinas) == 3:
                cachorro.disponivel = True
            self.__tela_cachorro.mostra_mensagem("Vacina adicionada com sucesso")
        else:
            self.__tela_cachorro.mostra_mensagem("Cachorro não encontrado")
        
    def pega_cachorro_por_chip(self, chip):
        for cachorro in self.__cachorros:
            if cachorro.chip == chip:
                return cachorro
        return None

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_cachorro,
                        2: self.altera_cachorro,
                        3: self.lista_cachorros,
                        4: self.exclui_cachorro,
                        5: self.adicionar_vacina,
                        0: self.retorna}

        while True:
            opcao_escolhida = self.__tela_cachorro.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            