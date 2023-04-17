class Animal:
    def __init__(self, chip: int, nome: str, raca: str,
                 vacinas: list(), disponivel: bool):
        self.__chip = chip
        self.__nome = nome
        self.__raca = raca

    # chip
    @property
    def chip(self):
        return self.__chip

    @chip.setter
    def chip(self, chip):
        self.__chip = chip

    # nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # raca
    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca
