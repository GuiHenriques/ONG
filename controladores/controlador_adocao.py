from entidades.adocao import Adocao
from telas.tela_adocao import TelaAdocao


class ControladorAdocao():
    def __init__(self, controlador_sistema):
        self.__adocoes = list()
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    def incluir_adocao_gato(self):
        self.__controlador_sistema.controlador_pessoa.lista_adotantes()
        self.__controlador_sistema.controlador_gato.lista_gatos_disponiveis()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        adotante = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_adocao["cpf"])
        gato = self.__controlador_sistema.controlador_gato.pega_gato_por_chip(dados_adocao["chip"])
        
        if len(gato.vacinas) < 3 or not gato.disponivel:
            self.__tela_adocao.mostra_mensagem("Gato não disponível para adoção")
            self.retornar()
        termo_responsa = self.__tela_adocao.assinar_termo_responsa()

        if (adotante and gato and termo_responsa):
            adocao = Adocao(dados_adocao["data"], gato, adotante)
            adocao.termo_responsa = True
            self.__adocoes.append(adocao)
            gato.disponivel = False
            self.__tela_adocao.mostra_mensagem("Adocao realizada com sucesso!")
        else:
            self.__tela_adocao.mostra_mensagem("Dados invalidos")
    
    def incluir_adocao_cachorro(self):
        self.__controlador_sistema.controlador_pessoa.lista_adotantes()
        self.__controlador_sistema.controlador_cachorro.lista_cachorros_disponiveis()
        while True:
            try:
                dados_adocao = self.__tela_adocao.pega_dados_adocao()
                cachorro = self.__controlador_sistema.controlador_cachorro.pega_cachorro_por_chip(dados_adocao["chip"])
                adotante = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_adocao["cpf"])
                if cachorro.tamanho() == 'G' and adotante.tipo_hab() == 'apartamento' and adotante.tam_hab() == 'P':
                    raise ValueError
                break
            except:
                print('Não é possível adotar um cachorro grande se você mora em um apartamento pequeno.' )



        adotante = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados_adocao["cpf"])
        cachorro = self.__controlador_sistema.controlador_cachorro.pega_cachorro_por_chip(dados_adocao["chip"])

        if len(cachorro.vacinas) < 3 or not cachorro.disponivel:
            self.__tela_adocao.mostra_mensagem("Gato não disponível para adoção")
            self.retornar()
        termo_responsa = self.__tela_adocao.assinar_termo_responsa()

        if not cachorro.disponivel:
            self.__tela_adocao.mostra_mensagem("Cachorro não disponível para adoção")
            self.retornar()
        
        if (adotante and cachorro and termo_responsa):
            adocao = Adocao(dados_adocao["data"], cachorro, adotante)
            adocao.termo_responsa = True
            self.__adocoes.append(adocao)
            cachorro.disponivel = False
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
            