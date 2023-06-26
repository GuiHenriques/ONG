from telas.tela_animal import TelaAnimal
from entidades.cachorro import Cachorro
from entidades.gato import Gato
from entidades.vacina import Vacina
from DAOs.animal_dao import AnimalDAO

class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_animal = TelaAnimal()
        self.__animal_DAO = AnimalDAO()
        self.__chip = None
        self.__tipo = None

    @property
    def tela_animal(self):
        return self.__tela_animal

    @property
    def animais(self):
        return self.__animais

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def inclui_animal(self):
        dados_animal = self.tela_animal.pega_dados_animal(self.tipo)
        if not dados_animal:
            return
        try:
            self.__chip = int(list(self.__animal_DAO.get_all())[-1].chip) + 1
        except IndexError:
            self.__chip = 1
        if self.tipo == "Cachorro":
            animal = Cachorro(
                self.__chip,
                dados_animal["nome"],
                dados_animal["raca"],
                dados_animal["idade"],
                dados_animal["tamanho"],
            )
        else:
            animal = Gato(
                self.__chip,
                dados_animal["nome"],
                dados_animal["raca"],
                dados_animal["idade"]
            )

        #self.animais.append(animal)
        self.__animal_DAO.add(animal)
        self.tela_animal.mostra_mensagem("Sucesso", f"{self.tipo} incluído com sucesso")
        print()
        return animal.chip

    def altera_animal(self):
        self.lista_animais()
        chip = self.pega_chip()
        animal = self.pega_animal_por_chip(chip)

        if not animal:
            return

        dados_animal = self.tela_animal.pega_dados_animal(self.tipo)
        if not dados_animal:
            return

        animal.nome = dados_animal["nome"]
        animal.raca = dados_animal["raca"]
        animal.idade = dados_animal["idade"]
        if self.tipo == "Cachorro":
            animal.tamanho = dados_animal["tamanho"]
        self.__animal_DAO.update(animal)

        self.tela_animal.mostra_mensagem("Sucesso", f"{self.tipo} alterado com sucesso")

    def lista_animais(self):
        condicao = (
            lambda animal: isinstance(animal, Cachorro)
            if self.tipo == "Cachorro"
            else isinstance(animal, Gato)
        )

        if len([animal for animal in self.__animal_DAO.get_all() if condicao(animal)]) == 0:
            self.tela_animal.mostra_mensagem("Erro", f"Nenhum {self.tipo} cadastrado")
            return

        lista_animais = []
        header = ( 
            ["Chip", "Nome", "Raça", "Idade", "Tamanho", "Nº de Vacinas"] if self.tipo == "Cachorro"
              else ["Chip", "Nome", "Raça", "Idade", "Nº de Vacinas"]
        )
        lista_animais.append(header)

        #for animal in self.animais:
        for animal in self.__animal_DAO.get_all():
            dados_animal = [animal.chip, animal.nome, animal.raca, int(animal.idade)]

            if self.tipo == "Cachorro" and isinstance(animal, Cachorro):
                dados_animal.append(animal.tamanho)
                dados_animal.append(len(animal.vacinas))
                lista_animais.append(dados_animal)

            elif self.tipo == "Gato" and isinstance(animal, Gato):
                dados_animal.append(len(animal.vacinas))
                lista_animais.append(dados_animal)

        self.tela_animal.mostra_animal(lista_animais)
        return True

    def lista_animais_disponiveis(self):
        condicao = (
            lambda animal: isinstance(animal, Cachorro) and animal.disponivel
            if self.tipo == "Cachorro"
            else isinstance(animal, Gato) and animal.disponivel
        )
        if len([animal for animal in self.__animal_DAO.get_all() if condicao(animal)]) == 0:
            self.tela_animal.mostra_mensagem("Erro", f"Nenhum {self.tipo} disponível")
            return None

        lista_animais = []
        header = ( 
            ["Chip", "Nome", "Raça", "Idade", "Tamanho", "Nº de Vacinas"] if self.tipo == "Cachorro"
              else ["Chip", "Nome", "Raça", "Idade", "Nº de Vacinas"]
        )
        lista_animais.append(header)

        #for animal in self.animais:
        for animal in self.__animal_DAO.get_all():
            if animal.disponivel:
                dados_animal = [animal.chip, animal.nome, animal.raca, int(animal.idade)]

                if isinstance(animal, Gato) and self.tipo == "Gato":
                    dados_animal.append(len(animal.vacinas))
                    lista_animais.append(dados_animal)

                elif isinstance(animal, Cachorro) and self.tipo == "Cachorro":
                    dados_animal.append(animal.tamanho)
                    dados_animal.append(len(animal.vacinas))
                    lista_animais.append(dados_animal)
                    
        self.tela_animal.mostra_animal(lista_animais)
        return True

    def exclui_animal(self):
        self.lista_animais()
        chip = self.pega_chip()
        animal = self.pega_animal_por_chip(chip)

        if animal:
            self.__animal_DAO.remove(chip)
            self.tela_animal.mostra_mensagem(
                "Sucesso", f"{self.tipo} excluído com sucesso"
            )

    def adicionar_vacina(self):
        self.lista_animais()
        chip = self.pega_chip()
        animal = self.pega_animal_por_chip(chip)

        if not animal:
            return

        dados_vacina = self.tela_animal.pega_dados_vacina()
        
        if not dados_vacina:
            return
        
        self.aplicar_vacina(animal, dados_vacina)
        self.__animal_DAO.update(animal)

    def aplicar_vacina(self, animal, dados_vacina):
        if dados_vacina["tipo"] == "Todas":
            if len(animal.vacinas) > 0:
                self.tela_animal.mostra_mensagem(
                    "Erro",
                    "Animal já possui alguma vacina, insira as outras separadamente",
                )
                return
            tipos = ["Raiva", "Lepitospirose", "Hepatite Infecciosa"]
            for tipo in tipos:
                vacina = Vacina(dados_vacina["data"], animal, tipo)
                animal.vacinas.append(vacina)

            self.tela_animal.mostra_mensagem("Sucesso", "Vacinas aplicadas com sucesso")
            animal.disponivel = True

        else:
            for vacina in animal.vacinas:
                if vacina.tipo == dados_vacina["tipo"]:
                    self.tela_animal.mostra_mensagem(
                        "Erro", f"Vacina de {vacina.tipo} já foi aplicada"
                    )
                    return

            vacina = Vacina(dados_vacina["data"], animal, dados_vacina["tipo"])
            animal.vacinas.append(vacina)
            if len(animal.vacinas) == 3:
                animal.disponivel = True
            self.tela_animal.mostra_mensagem("Sucesso", "Vacina aplicada com sucesso")

    def pega_chip(self):
        while True:
            try:
                chip = int(self.tela_animal.seleciona_animal())
                return chip
            except ValueError:
                self.tela_animal.mostra_mensagem("Erro", "Chip Inválido")

    def pega_animal_por_chip(self, chip: int):
        #for animal in self.animais:
        for animal in self.__animal_DAO.get_all():
            print(animal.chip)
            if animal.chip == chip:
                return animal
        return None

    def tipo_animal(self):
        self.tipo = self.tela_animal.seleciona_tipo_animal()
        if not self.tipo:
            self.retornar()
        self.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_animal,
            2: self.altera_animal,
            3: self.lista_animais,
            4: self.lista_animais_disponiveis,
            5: self.exclui_animal,
            6: self.adicionar_vacina,
            0: self.tipo_animal,
        }

        while True:
            opcao_escolhida = self.tela_animal.tela_opcoes(self.tipo)
            lista_opcoes[opcao_escolhida]()
