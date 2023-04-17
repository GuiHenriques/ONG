from abc import ABC, abstractmethod

class UsuarioBU(ABC):
    @abstractmethod
    def __init__(self, cpf: str, dias_de_emprestimo: int):
        self.__cpf = cpf
        self.__dias_de_emprestimo = dias_de_emprestimo
    
    #cpf
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    #dias_de_emprestimo
    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo
    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo):
        self.__dias_de_emprestimo = dias_de_emprestimo
    
    def emprestar(self, titulo_livro: str):
        mensagem = f"pegou emprestado o livro: {titulo_livro}"
        return mensagem
    
    def devolver(self, titulo_livro: str):
        mensagem = f"devolveu o livro: {titulo_livro}"
        return mensagem


class Funcionario(UsuarioBU):
    @abstractmethod
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento
    
    #departamento
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento
    
    @abstractmethod
    def emprestar(self, titulo_livro: str):
        mensagem = 
        return f"do departamento {self.__departamento} {mensagem} com {super().dias_de_emprestimo} dias de prazo"
        mensagem = super().emprestar(titulo_livro)
    
    @abstractmethod
    def devolver(self, titulo_livro: str):
        mensagem = super().devolver(titulo_livro)
        return f"do departamento {self.__departamento} {mensagem}"
           

class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    #matricula
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    def emprestar(self, titulo_livro: str):
        mensagem = super().emprestar(titulo_livro)
        return f"Aluno de matricula {self.__matricula} {mensagem}"

    def devolver(self, titulo_livro: str):
        mensagem = super().devolver(titulo_livro)
        return f"Aluno de matricula {self.__matricula} {mensagem}"


class Professor(Funcionario):
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo=20):
        super().__init__(departamento, cpf, dias_de_emprestimo)
    
    def emprestar(self, titulo_livro: str):
        mensagem = super().emprestar(titulo_livro)
        return f"Professor {mensagem}"

    def devolver(self, titulo_livro: str):
        mensagem = super().devolver(titulo_livro)
        return f"Professor {mensagem}"


class Administrativo(Funcionario):
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo=10):
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_livro: str):
        mensagem = super().emprestar(titulo_livro)
        return f"Funcionario administrativo {mensagem}"

    def devolver(self, titulo_livro: str):
        mensagem = super().devolver(titulo_livro)
        return f"Funcionario administrativo {mensagem}"


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf, dias_de_emprestimo, matricula):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

        if self.__elaborando_tese == True:
            self.__dias_de_emprestimo *= 2

    #elaborando_tese
    @property
    def elaborando_tese(self):
        return self.__elaborando_tese
    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro: str):
        mensagem = super().emprestar(titulo_livro)
        return f"{mensagem} com {self.__dias_de_emprestimo} dias de prazo"
        

    def devolver(self, titulo_livro: str):
        mensagem = super().devolver(titulo_livro)
        return f"{mensagem}"