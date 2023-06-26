from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao
from DAOs.doacao_dao import DoacaoDAO

class ControladorDoacao():

    def __init__(self, controlador_sistema):
        #self.__doacoes = list()
        self.__doacao_DAO = DoacaoDAO()
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
        #self.doacoes.append(doacao)
        self.__doacao_DAO.add(doacao)
        
        self.tela_doacao.mostra_mensagem("Sucesso", "Doação realizada com sucesso!")
    
    def incluir_doacao(self):
        self.__controlador_sistema.controlador_pessoa.tipo = "Doador"
        self.__controlador_sistema.controlador_pessoa.inclui_pessoa()
    
    def listar_doacoes(self):
        #if len(self.doacoes) == 0:
        if len(self.__doacao_DAO.get_all()) ==0:    
            self.tela_doacao.mostra_mensagem("Erro", "Nenhuma doacao cadastrada")
            return None

        dados_doacao = []
        for doacao in self.__doacao_DAO.get_all():
            dados_doacao.append({
                "data": doacao.data,
                "animal": doacao.animal.nome,
                "doador": doacao.doador.nome,
                "motivo": doacao.motivo})
        self.tela_doacao.mostra_doacao(dados_doacao)
    
    def listar_doacoes_por_periodo(self):
        #if len(self.doacoes) == 0:
        if len(self.__doacao_DAO.get_all()) == 0:    
            self.tela_doacao.mostra_mensagem("Erro", "Nenhuma doacao cadastrada")
            return None
        
        n_doacoes = 0
        data_inicio, data_fim = self.tela_doacao.pega_datas()
        
        #for doacao in self.doacoes:
        for doacao in self.__doacao_DAO.get_all():
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
