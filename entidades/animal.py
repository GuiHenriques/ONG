class Animal():
    def __init__(self, chip: int, nome: str, raca: str, idade:int, vacinas: list, disponivel: bool):
        self.__chip = chip
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade
        self.__vacinas = vacinas
        self.__disponivel = disponivel
    
    @property
    def chip(self):
        return self.__chip
    
    @chip.setter
    def chip(self, chip):
        self.__chip = chip
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def raca(self):
        return self.__raca
    
    @raca.setter
    def raca(self, raca):
        self.__raca = raca
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
        
    @property
    def vacinas(self):
        return self.__vacinas
    
    #fazer setter de vacinas?
    @property
    def adocao_atual(self):
        return self.__adocao_atual

    @property
    def disponivel(self):
        return self.__disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        self.__disponivel = disponivel
