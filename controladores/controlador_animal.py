from telas.tela_animal import TelaAnimal
from entidades.cachorro import Cachorro
from entidades.gato import Gato
from entidades.vacina import Vacina

class ControladorAnimal():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_animal = TelaAnimal()
        self.__animais = [Cachorro("Rex", "Vira-lata", "G"), Gato("Mingau", "Persa")]
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
        if self.tipo == "Cachorro":
            animal = Cachorro(dados_animal["nome"], dados_animal["raca"], dados_animal["tamanho"])
        else:
            animal = Gato(dados_animal["nome"], dados_animal["raca"])
        
        self.animais.append(animal)
        self.tela_animal.mostra_mensagem(f"{self.tipo} incluído com sucesso")
        return animal

    def altera_animal(self):
        self.lista_animais()
        chip = self.pega_chip()
        animal = self.pega_animal_por_chip(chip)


        if not animal:
            return
        
        dados_animal = self.tela_animal.pega_dados_animal(self.tipo)

        animal.nome = dados_animal["nome"]
        animal.raca = dados_animal["raca"]
        if self.tipo == "Cachorro":
            animal.tamanho = dados_animal["tamanho"]

        self.tela_animal.mostra_mensagem(f"{self.tipo} alterado com sucesso")

    def lista_animais(self):
        condicao = lambda animal: isinstance(animal, Cachorro) if self.tipo == "Cachorro" else isinstance(animal, Gato)
        
        if len([animal for animal in self.animais if condicao(animal)]) == 0:
            self.tela_animal.mostra_mensagem(f"Nenhum {self.tipo} cadastrado")
            return
        
        for animal in self.animais:
            dados_animal = {"chip": animal.chip,"nome": animal.nome, "raca": animal.raca, "vacinas": animal.vacinas}
            
            if self.tipo == "Cachorro" and isinstance(animal, Cachorro):
                    dados_animal["tamanho"] = animal.tamanho
                    self.tela_animal.mostra_animal(dados_animal)
            
            elif self.tipo == "Gato" and isinstance(animal, Gato):
                    self.tela_animal.mostra_animal(dados_animal)
        return True

    def lista_animais_disponiveis(self):
        condicao = lambda animal: isinstance(animal, Cachorro) and animal.disponivel if self.tipo == "Cachorro" else isinstance(animal, Gato) and animal.disponivel
        if len([animal for animal in self.animais if condicao(animal)]) == 0:
            self.tela_animal.mostra_mensagem(f"Nenhum {self.tipo} disponível")
            return None
        
        for animal in self.animais:
            if animal.disponivel:
                
                dados_animal = {"chip": animal.chip, "nome": animal.nome, "raca": animal.raca, "vacinas": animal.vacinas}
                
                if isinstance(animal, Gato) and self.tipo == "Gato":
                    self.tela_animal.mostra_animal(dados_animal)
                        
                elif isinstance(animal, Cachorro) and self.tipo == "Cachorro":
                    dados_animal["tamanho"] = animal.tamanho
                    self.tela_animal.mostra_animal(dados_animal)
        return True
    
    def exclui_animal(self):
        self.lista_animais()
        chip = self.pega_chip()
        animal = self.pega_animal_por_chip(chip)


        if animal:
            self.animais.remove(animal)
            self.tela_animal.mostra_mensagem(f"{self.tipo} excluído com sucesso")
    
    def adicionar_vacina(self):
        self.lista_animais()
        chip = self.pega_chip()
        animal = self.pega_animal_por_chip(chip)
        
        if not animal:
            return
        
        dados_vacina = self.tela_animal.pega_dados_vacina()
        self.aplicar_vacina(animal, dados_vacina)
  
    def aplicar_vacina(self, animal, dados_vacina):
        if dados_vacina["tipo"] == "Todas":
            if len(animal.vacinas) > 0:
                self.tela_animal.mostra_mensagem("Animal já possui alguma vacina, insira as outras separadamente")
                return
            tipos = ["Raiva", "Lepitospirose", "Hepatite Infecciosa"]
            for tipo in tipos:
                vacina = Vacina(dados_vacina["data"], animal, tipo)
                animal.vacinas.append(vacina)
            
            self.tela_animal.mostra_mensagem("Vacinas aplicadas com sucesso")
            animal.disponivel = True

        else:
            for vacina in animal.vacinas:
                if vacina.tipo == dados_vacina["tipo"]:
                    self.tela_animal.mostra_mensagem(f"Vacina de {vacina.tipo} já foi aplicada")
                    return
                
            vacina = Vacina(dados_vacina["data"], animal, dados_vacina["tipo"])
            animal.vacinas.append(vacina)
            self.tela_animal.mostra_mensagem("Vacina aplicada com sucesso")

    def pega_chip(self):
        while True:    
            try:
                chip = int(self.tela_animal.seleciona_animal())
                return chip
            except ValueError:
                self.tela_animal.mostra_mensagem("Chip Inválido")
    
    def pega_animal_por_chip(self, chip):
        for animal in self.animais:
            if animal.chip == chip:
                return animal
        self.tela_animal.mostra_mensagem("Animal não encontrado")
        return None
    
    def tipo_animal(self):
        self.tipo = self.tela_animal.seleciona_tipo_animal()
        if not self.tipo: self.retornar()
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
            0: self.retornar
        }

        while True:
            opcao_escolhida = self.tela_animal.tela_opcoes(self.tipo)
            print('return', opcao_escolhida)
            lista_opcoes[opcao_escolhida]()