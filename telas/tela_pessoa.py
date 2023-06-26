from telas.abstract_tela import AbstractTela
from datetime import date, datetime
import PySimpleGUI as sg

class TelaPessoa(AbstractTela):
    def __init__(self):
        self.__window = None

    def tela_opcoes(self, tipo):
        layout = self.define_layout_button([f'Incluir {tipo}', f'Alterar {tipo}', f'Listar {tipo}s', f'Excluir {tipo}'])
                
        self.__window = sg.Window(f'{tipo}', size=(500, 300)).Layout(layout)

        while True:
            button, values = self.open()
            
            if button == sg.WINDOW_CLOSED or button == 'Sair':
                self.close()
                return 0

            if button:
                self.close()
                return button
            
    def seleciona_tipo_pessoa(self):
        layout = self.define_layout_radio(['Adotante', 'Doador'])
        self.__window = sg.Window('Tipo Pessoa').Layout(layout)

        button, values = self.open()
        self.close()

        if button == sg.WINDOW_CLOSED or button == "Sair":
            return None

        return "Adotante" if values[1] else "Doador"

    def pega_dados_pessoa(self, tipo):
        size = 16
        layout = [
            [sg.Text('Nome:', size=size), sg.InputText("", key='nome')],
            [sg.Text('CPF:', size=size), sg.InputText('', key='cpf')],
            [sg.Text('Dia:',size=size),sg.Slider(range=(1,31), orientation='h',size=(35, 12),key='dia')],
            [sg.Text('Mês:', size=size), sg.Slider(range=(1, 12), orientation='h',size=(35,12), key='mes')],
            [sg.Text('Ano:', size=size), sg.Slider(range=(1920, 2005), orientation='h',size=(35,12), key='ano')],
            [sg.Text('Endereço:',size = (15,1)), sg.InputText("",key='endereco')],
        ]
    
        if tipo == 'Adotante':
            layout_extra = [
            [sg.Text('Tipo de habitação:', size=size),sg.Combo(('Casa','Apartamento'), key='cb_tipo_hab')],
            [sg.Text('Tamanho da habitação:',size=size),sg.Combo(('Pequeno','Médio','Grande'),key = 'cb_tam_hab')],
            [sg.Text('Possui outros animais:', size=size),sg.Combo(('Sim','Não'), key='cb_outros_animais')],
            ]
            for line  in layout_extra:
                layout.append(line)
        
        layout.append([sg.Button('Confirmar'), sg.Button('Cancelar')])

        self.__window = sg.Window(f'Gerenciando {tipo}').Layout(layout)
        while True:
            button, values = self.open()
            if button == sg.WINDOW_CLOSED or button == "Cancelar":
                self.close()
                return None
            
            data = f"{int(values['dia'])}/{int(values['mes'])}/{int(values['ano'])}"
            data_f = datetime.strptime(data, '%d/%m/%Y').date()
            
            if self.valores_vazios(values) and self.valor_inteiro(values['cpf']):
                    self.close()
                    if tipo == 'Adotante':
                        return {"nome": values['nome'], "cpf": values['cpf'], "data": data_f, "endereco": values['endereco'], "tipo_hab": values['cb_tipo_hab'], "tam_hab": values['cb_tam_hab'], "outros_animais": values['cb_outros_animais']}
                    else:
                        return {"nome": values['nome'], "cpf": values['cpf'], "data": data_f, "endereco": values['endereco']}
        
    def mostra_pessoa(self,dados_pessoa):
        width = [10, 10, 10, 10, 10, 10, 15] if len(dados_pessoa[0]) == 7 else [17,17,17,17]
        layout = [
            [sg.Table(values=dados_pessoa[1:], headings=dados_pessoa[0], num_rows=max(len(dados_pessoa), 8), row_height=25, justification='center', auto_size_columns=False, col_widths=width)],
            [sg.Txt("", size=20), sg.Button("Ok", size=(10,1), pad=(10))],
        ]

        self.__window = sg.Window("Lista de Animais", layout, size=(700, 300))

        button, values = self.open()

        if button == sg.WINDOW_CLOSED:
            exit(0)

        if button == "Ok":
            self.close()
            return


    def pega_cpf(self):
        layout = [
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf', size=15)],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]

        self.__window = sg.Window('Pega CPF').Layout(layout)

        while True:
            button, values = self.open()
            if button == sg.WINDOW_CLOSED or button == "Cancelar":
                self.close()
                return None
            
            if self.valores_vazios(values):
                if not self.valor_inteiro(values['cpf']):
                    self.mostra_mensagem("Erro", 'CPF inválido')
                else:
                    self.close()
                    return (values['cpf'])
        

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()