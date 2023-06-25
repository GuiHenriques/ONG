from telas.abstract_tela import AbstractTela
from datetime import date, datetime
import PySimpleGUI as sg

class TelaPessoa(AbstractTela):
    def __init__(self):
        self.__window = None
        self.seleciona_tipo_pessoa()

    def tela_opcoes_pessoa(self, tipo):
        self.init_components(tipo)
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
        if tipo == 'Adotante':
            layout = [
            [sg.Text(f'-------- Dados {tipo} --------', font =('Arial', 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(default_text='', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            #[sg.Spin(values=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'),initial_value='selecione o dia',key = 'sp_spin1')],
            [sg.Text('Dia:',size=(15,1)),sg.Slider(range=(1,31), orientation='h',size =(10,10),key='dia'),
            sg.Text('Mês:', size=(15, 1)), sg.Slider(range=(1, 12), orientation='h',size =(10,10), key='mes'),
            sg.Text('Ano:', size=(15, 1)), sg.Slider(range=(1920, 2005), orientation='h',size =(10,10), key='ano')],
            [sg.Text('Endereço:',size = (15,1)), sg.InputText(default_text='',key='endereco')],
            [sg.Text('Tipo de habitação:', size=(16, 1)),sg.Combo(('Casa','Apartamento'), key='cb_tipo_hab')],
            [sg.Text('Tamanho da habitação:',size = (16,1)),sg.Combo(('Pequeno','Médio','Grande'),key = 'cb_tam_hab')],
            [sg.Text('Possui outros animais:', size=(16, 1)),sg.Combo(('Sim','Não'), key='cb_outros_animais')],
            #[sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            [sg.Button('Confirmar')]
            ]

            self.__window = sg.Window(f'Gerenciando {tipo}').Layout(layout)
            button, values = self.__window.Read()
            uniao_data = str(int(values['dia']))+'/'+ str(int(values['mes'])) +'/' + str(int(values['ano']))
            data = datetime.strptime(uniao_data, '%d/%m/%Y').date()
            nome = values['nome']
            cpf = values['cpf']
            endereco = values['endereco']
            tipo_hab = values['cb_tipo_hab']
            tam_hab = values['cb_tam_hab']
            outros_animais = values['cb_outros_animais']
            self.close()
            return {'nome': nome, 'cpf': cpf,'data_nascimento':data,'endereco': endereco,'tipo_hab':tipo_hab,'tam_hab':tam_hab,'outros_animais':outros_animais}
        if tipo == 'Doador':
            layout = [
                [sg.Text(f'-------- Dados {tipo} --------', font=('Arial', 25))],
                [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                [sg.Text('Dia:', size=(15, 1)), sg.Slider(range=(1, 31), orientation='v', size=(10, 10), key='dia'),
                 sg.Text('Mês:', size=(15, 1)), sg.Slider(range=(1, 12), orientation='v', size=(10, 10), key='mes'),
                 # [sg.popup_get_date(title = 'Data de nascimento')],
                 sg.Text('Ano:', size=(15, 1)),
                 sg.Slider(range=(1920, 2005), orientation='v', size=(10, 10), key='ano')],
                [sg.Text('Endereço:', size=(15, 1)), sg.InputText('', key='endereco')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]


            self.__window = sg.Window(f'Gerenciando {tipo}').Layout(layout)
            button, values = self.__window.Read()
            uniao_data = str(int(values['dia'])) + '/' + str(int(values['mes'])) + '/' + str(int(values['ano']))
            data = datetime.strptime(uniao_data, '%d/%m/%Y').date()
            nome = values['nome']
            cpf = values['cpf']
            endereco = values['endereco']
            self.close()
            return {'nome': nome, 'cpf': cpf,'data' : data, 'endereco': endereco}
    def mostra_pessoa(self,dados_pessoa):
        string_todos_pessoa = str
        for dado in dados_pessoa:
            string_todos_pessoa = string_todos_pessoa + "Nome: " + dado["nome"] + '\n'
            string_todos_pessoa = string_todos_pessoa + "Cpf: " + dado["cpf"] + '\n'
            string_todos_pessoa = string_todos_pessoa + "Data de nascimento: " + dado["data"] + '\n'
            string_todos_pessoa = string_todos_pessoa + "Endereço: " + dado["endereco"] + '\n'
            if dado['tipo_hab'] in dados_pessoa:
                string_todos_pessoa = string_todos_pessoa + "Tipo de habitação: " + dado["tipo_hab"] + '\n'
                string_todos_pessoa = string_todos_pessoa + "Tamanho da habitação: " + dado["tam_hab"] + '\n'
                string_todos_pessoa = string_todos_pessoa + "Possui outros animais: " + dado["outros_animais"] + '\n'
        sg.Popup('-------- LISTA DE AMIGOS ----------', string_todos_pessoa)

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
        if tipo == 'Adotante':
            layout = [
                [sg.Text(f'-------- {tipo} --------', font = ('Arial', 26))],
                [sg.Radio(f'Incluir {tipo}', "RD1", key='1')],
                [sg.Radio(f'Alterar {tipo}', "RD1", key='2')],
                [sg.Radio(f'Listar {tipo}s', "RD1", key='3')],
                [sg.Radio(f'Excluir {tipo}', "RD1", key='4')],
                [sg.Radio('Retornar', "RD1", key='0')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        if tipo == 'Doador':
            layout = [
                [sg.Text(f'-------- {tipo} --------', font=('Arial', 26))],
                [sg.Radio(f'Incluir {tipo}', "RD1", key='1')],
                [sg.Radio(f'Alterar {tipo}', "RD1", key='2')],
                [sg.Radio(f'Listar {tipo}es', "RD1", key='3')],
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

    def mostra_mensagem(self, msg):
        sg.popup(msg,title='Erro')
    def close(self):
        self.__window.Close()