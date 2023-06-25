from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao

class ControladorDoacao():

    def __init__(self, controlador_sistema):
        self.__doacoes = list()
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema

    @property
    def doacoes(self):
        return self.__doacoes
    
    @property
    def tela_doacao(self):
        return self.__tela_doacao
    
    def inclui_doacao_direta(self, animal, pessoa):
        dados_doacao = self.tela_doacao.pega_dados_doacao()
        doacao = Doacao(dados_doacao["data"], animal, pessoa, dados_doacao["motivo"])
        self.doacoes.append(doacao)
        self.tela_doacao.mostra_mensagem("Sucesso", "Doação realizada com sucesso!")
    
    def incluir_doacao(self):
        self.__controlador_sistema.controlador_pessoa.tipo = "Doador"
        self.__controlador_sistema.controlador_pessoa.inclui_pessoa()
    
    def listar_doacoes(self):
        if len(self.doacoes) == 0:
            self.tela_doacao.mostra_mensagem("Erro", "Nenhuma doacao cadastrada")
            return None

        for doacao in self.doacoes:
            dados_doacao = {
                "data": doacao.data,
                "animal": doacao.animal.nome,
                "doador": doacao.doador.nome,
                "motivo": doacao.motivo}
            self.tela_doacao.mostra_doacao(dados_doacao)
    
    def listar_doacoes_por_periodo(self):
        if len(self.__doacoes) == 0:
            self.tela_doacao.mostra_mensagem("Erro", "Nenhuma doacao cadastrada")
            return None
        
        n_doacoes = 0
        data_inicio = self.tela_doacao.pega_data('Data de inicio (DD/MM/AAAA): ')
        data_fim = self.tela_doacao.pega_data('Data de fim (DD/MM/AAAA): ')
        
        for doacao in self.__doacoes:
            if doacao.data >= data_inicio and doacao.data <= data_fim:
                dados_doacao = {
                    "data": doacao.data,
                    "animal": doacao.animal.nome,
                    "doador": doacao.doador.nome,
                    "motivo": doacao.motivo}
                self.tela_doacao.mostra_doacao(dados_doacao)
                n_doacoes += 1
        
        if n_doacoes == 0:
            self.tela_doacao.mostra_mensagem("Erro", "Nenhuma doacao cadastrada no periodo")
  
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao,
            2: self.listar_doacoes,
            3: self.listar_doacoes_por_periodo,
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.tela_doacao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            