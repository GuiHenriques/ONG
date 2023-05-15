from telas.abstract_tela import AbstractTela
from datetime import date,datetime


class TelaPessoa(AbstractTela):
        
    def tela_opcoes(self):
        print("-------- Pessoa ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adotante")
        print("2 - Alterar Adotante")
        print("3 - Listar Adotantes")
        print("4 - Excluir Adotante")
        print("5 - Incluir Doador")
        print("6 - Alterar Doador")
        print("7 - Listar Doadores")
        print("8 - Excluir Doador")
        print("0 - Retornar")
    
        opcao = self.le_opcao("Escolha uma opcao: ", [0,1,2,3,4,5,6,7,8])
        return opcao
    
    def pega_dados_adotante(self):
        print('----------DADOS ADOTANTE-------------')
        nome = input('Nome: ')
        cpf = input('Cpf: ')
        data_nascimento = input('Data de Nascimento (DD/MM/AAAA): ')
        data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        endereco = input('Endereço: ')
        tipo_hab = input('Tipo de habitacao (Casa, Ap):')
        tam_hab = input('Insira o tamanho da sua habitacao: p, m ou g ')
        outros_animais = input('Possui outros animais (Sim, Nao): ')
        
        # tratamento da idade caso seja menor de idade:
        today = date.today()
        age = today.year - data_f.year - ((today.month, today.day) < (data_f.month, data_f.day))
        #if age < 18:
            #raise alguma exception.Finalizar o programa ou pedir a data de novo?
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_f, "endereco": endereco,"tipo_hab": tipo_hab, "tam_hab": tam_hab, "outros_animais": outros_animais}

    def pega_dados_doador(self):
        print('----------DADOS DOADOR-------------')
        nome = input('Nome: ')
        cpf = input('Cpf: ')
        while True:
            try:
                data_nascimento = input('Data de Nascimento (DD/MM/AAAA): ')
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                today = date.today()
                age = today.year - data_f.year - ((today.month, today.day) < (data_f.month, data_f.day))
                break
            except ValueError:
                self.mostra_mensagem('Data inválida')
        # o tratamento da idade caso seja menor de idade:
        # if age < 18:
        # raise alguma exception.Finalizar o programa ou pedir a data de novo?
        endereco = input('Endereço: ')
        animal = input('Deseja doar gato ou cachorro?: ').lower()
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_f, "endereco": endereco, "animal": animal}

    def mostra_adotante(self, dados_adotante):
        print('------------ ADOTANTES ------------')
        print('Nome:', dados_adotante['nome'])
        print('Cpf:', dados_adotante['cpf'])
        print('Data de nascimento:', dados_adotante['data_nascimento'])
        print('Endereco:', dados_adotante['endereco'])
        print('Tipo de habitacao (Casa, Ap):', dados_adotante['tipo_hab'])
        print('Tamanho da habitacao (P, M, G):', dados_adotante['tam_hab'])
        print('Possui outros animais (Sim, Nao)', dados_adotante['outros_animais'])
        print()

    def mostra_doador(self, dados_doador):
        print('------------DOADORES------------')
        print('Nome:', dados_doador['nome'])
        print('Cpf:', dados_doador['cpf'])
        print('Data de nascimento:', dados_doador['data_nascimento'])
        print('Endereco:', dados_doador['endereco'])
        print()

    def seleciona_pessoa_por_cpf(self):
        cpf = input('Insira o cpf da pessoa: ')
        return cpf
    
    def seleciona_animal(self):
        animal = input('Deseja selecionar gato ou cachorro?: ').lower()
        return animal