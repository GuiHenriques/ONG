from telas.abstract_tela import AbstractTela
from datetime import date, datetime
import PySimpleGUI as sg

class TelaPessoa(AbstractTela):
    def __init__(self):
        self.__window = None
        self.seleciona_tipo_pessoa()

    '''def tela_opcoes(self, tipo):
        print(f"-------- {tipo} ----------")
        print("Escolha a opcao")
        print(f"1 - Incluir {tipo}")
        print(f"2 - Alterar {tipo}")
        print(f"3 - Listar {tipo}s") if tipo == 'Adotante' else print(f"3 - Listar {tipo}es")
        print(f"4 - Excluir {tipo}")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha uma opcao: ", [0, 1, 2, 3, 4])
        return opcao'''

    def tela_opcoes_pessoa(self):
        self.init_components(self.tipo)
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def tela_escolhe_pessoa(self):
    #metodo para pegar se quer adotante ou doador

        self.seleciona_tipo_pessoa()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 'Adotante'
        if values['2']:
            opcao = 'Doador'
        if values ['0'] or button in (None, 'Cancelar'):
            opcao = None

        self.close()
        return opcao

    def pega_dados_pessoa(self, tipo):
        print(f'----------Dados {tipo}-------------')
        nome = input('Nome: ')
        cpf = self.pega_cpf()
        while True:
            try:
                data_nascimento = input('Data de Nascimento (DD/MM/AAAA): ')
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                today = date.today()
                age = today.year - data_f.year - ((today.month, today.day) < (data_f.month, data_f.day))
                if age < 18:
                    print('Menores de idade não podem adotar um animal.')
                else:
                    break
            except ValueError:
                self.mostra_mensagem('Data inválida, insira a data no formato DD/MM/AAAA. ')
        endereco = input('Endereço: ')
        if tipo == 'Adotante':
            while True:
                try:
                    tipo_hab = input('Tipo de habitação (casa, apartamento):').lower()
                    if tipo_hab == 'casa' or tipo_hab == 'apartamento':
                        break
                    else:
                        raise ValueError
                except ValueError:
                    self.mostra_mensagem('Habitação inválida, insira ou "casa" ou "apartamento" como resposta. ')

            while True:
                try:
                    tam_hab = input('Tamanho da habitacao (P, M, G): ').upper()
                    if tam_hab in ['P', 'M', 'G']:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    self.mostra_mensagem('Tamanho inválido, insira P, M ou G como resposta. ')

            while True:
                try:
                    outros_animais = input('Possui outros animais? (Sim, Nao): ').upper()[0]
                    if outros_animais in ['S', 'N']:
                        break
                    else:
                        raise ValueError
                except ValueError:
                    self.mostra_mensagem('Resposta inválida, insira "Sim" ou "Nao" como resposta. ')
            return {"nome": nome, "cpf": cpf, "data_nascimento": data_f, "endereco": endereco, "tipo_hab": tipo_hab,
                    "tam_hab": tam_hab, "outros_animais": outros_animais}

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_f, "endereco": endereco}

    def mostra_pessoa(self, dados_pessoa):
        print('------------ Pessoa ------------')
        print('Nome:', dados_pessoa['nome'])
        print('Cpf:', dados_pessoa['cpf'])
        print('Data de nascimento:', dados_pessoa['data_nascimento'])
        print('Endereco:', dados_pessoa['endereco'])
        if 'tipo_hab' in dados_pessoa:
            print('Tipo de habitacao:', dados_pessoa['tipo_hab'])
            print('Tamanho da habitacao:', dados_pessoa['tam_hab'])
            print('Possui outros animais:', dados_pessoa['outros_animais'])
        print()

    '''def seleciona_tipo_pessoa(self):
        print("-------- Pessoa ----------")
        print("1 - Adotante")
        print("2 - Doador")
        print("0 - Retornar")

        tipo = self.le_opcao("Escolha a opção: ", [0, 1, 2])
        if tipo == 0: return None

        animal = "Adotante" if tipo == 1 else "Doador"
        return animal'''

    def seleciona_tipo_pessoa(self):
        #equivalente ao tela_opcoes nos outros controladores, porem
        #eh desse jeito pois eh a tela intermediaria
        sg.ChangeLookAndFeel('DarkBlue4')
        layout = [
            [sg.Text('-------- Adotante ou Doador ----------', font=("Arial", 25))],
            [sg.Text('Escolha sua opção', font=("Arial", 15))],
            [sg.Radio('Adotante', "RD1", key='1')],
            [sg.Radio('Doador', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Pessoas').Layout(layout)

    def init_components(self, tipo):
        layout = [
            [sg.Text(f'-------- {tipo} --------', font = ('Arial', 26))],
            [sg.Radio(f'Incluir {tipo}', "RD1", key='1')],
            [sg.Radio(f'Alterar {tipo}', "RD1", key='2')],
            [sg.Radio(f'Listar {tipo}s', "RD1", key='3')],
            [sg.Radio(f'Excluir {tipo}', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window(f'Gerenciando {tipo}').Layout(layout)


    def pega_cpf(self):
        while True:
            try:
                cpf = input('CPF: ')
                if not cpf.isnumeric():
                    raise ValueError
                break
            except ValueError:
                self.mostra_mensagem('CPF inválido, insira apenas números. ')
        return cpf

    def close(self):
        self.__window.Close()