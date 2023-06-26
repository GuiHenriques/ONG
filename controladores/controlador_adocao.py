from entidades.adocao import Adocao
from entidades.cachorro import Cachorro
from telas.tela_adocao import TelaAdocao


class ControladorAdocao():
    def __init__(self, controlador_sistema):
        self.__adocoes = list()
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def adocoes(self):
        return self.__adocoes
    
    @property
    def tela_adocao(self):
        return self.__tela_adocao

    def incluir_adocao(self):
        dados = self.verifica_adocao()
        if not dados:
            return
        print(dados)
        data, animal, adotante = dados["data"], dados["animal"], dados["adotante"]
        
        if isinstance(animal, Cachorro) and animal.tamanho == "G" and adotante.tipo_hab == "Apartamento" and adotante.tam_hab == "P":
            self.tela_adocao.mostra_mensagem("Erro", "Não é possível adotar um cachorro de grande porte em um apartamento pequeno")
            return

        # verficar se é possivel adotar um animal não disponivel pelo numero do chip quando existe um animal disponivel
        # verifica se o animal tem as 3 vacinas

        if not self.tela_adocao.assinar_termo_responsa():
            self.tela_adocao.mostra_mensagem("Erro", "Termo de responsabilidade não assinado")
            return

        adocao = Adocao(data, animal, adotante)
        print("deu bom")
        adocao.termo_responsa = True
        animal.disponivel = False
        self.adocoes.append(adocao)
        self.tela_adocao.mostra_mensagem("Sucesso", "Adoção realizada com sucesso")


    def verifica_adocao(self):
        # verifica lista de adotantes vazia
        self.__controlador_sistema.controlador_pessoa.tipo = "Adotante"
        if not self.__controlador_sistema.controlador_pessoa.lista_pessoas():
            return None
        print("tem adotante na lista")
        # verfica lista de animais vazia
        tipo_animal = self.__controlador_sistema.controlador_animal.tela_animal.seleciona_tipo_animal()
        self.__controlador_sistema.controlador_animal.tipo = tipo_animal

        if not self.__controlador_sistema.controlador_animal.lista_animais_disponiveis():
            return None
        print("tem animal na animais")
        
        dados = self.tela_adocao.pega_dados_adocao()
        # verifica se dados foram preenchidos
        if not dados:
            return None

        # verifica animal invalido
        animal = self.__controlador_sistema.controlador_animal.pega_animal_por_chip(dados["chip"])
        print(animal.nome)
        if not animal:
            return None
        


        if not animal.disponivel:
            self.tela_adocao.mostra_mensagem("Erro", "Animal não disponível para adoção")
            return None
        
        # verifica pessoa invalida
        pessoa = self.__controlador_sistema.controlador_pessoa.pega_pessoa_por_cpf(dados["cpf"])
        if not pessoa:
            return None

        return {"animal": animal, "adotante": pessoa, "data": dados["data"]}


    def listar_adocoes(self):
        if len(self.adocoes) == 0:
            self.tela_adocao.mostra_mensagem("Erro", "Nenhuma adocao cadastrada")
            return None

        for adocao in self.adocoes:
            dados_adocao = {
                "data": adocao.data,
                "animal": adocao.animal.nome,
                "adotante": adocao.adotante.nome,}

        self.tela_adocao.mostra_adocao(dados_adocao)
    
    def listar_adocoes_por_periodo(self):
        if len(self.adocoes) == 0:
            self.tela_adocao.mostra_mensagem("Erro", "Nenhuma adocao cadastrada")
        else:
            n_adocoes = 0
            data_inicial = self.tela_adocao.pega_data("Data inicial (DD/MM/AAAA): ")
            data_final = self.tela_adocao.pega_data("Data final (DD/MM/AAAA): ")
           
            for adocao in self.adocoes:
                if adocao.data >= data_inicial and adocao.data <= data_final:
                    dados_adocao = {
                        "data": adocao.data,
                        "animal": adocao.animal.nome,
                        "adotante": adocao.adotante.nome,}
                    
                    self.tela_adocao.mostra_adocao(dados_adocao)
                    n_adocoes += 1

            if n_adocoes == 0:
                self.tela_adocao.mostra_mensagem("Erro", "Nenhuma adocao cadastrada no periodo")
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.listar_adocoes,
            3: self.listar_adocoes_por_periodo,
            0: self.retornar
        }


        while True:
            opcao_escolhida = self.tela_adocao.tela_opcoes()
            lista_opcoes[opcao_escolhida]()
            