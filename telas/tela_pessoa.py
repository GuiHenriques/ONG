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
        
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_f, "endereco": endereco,"tipo_hab": tipo_hab, "tam_hab": tam_hab, "outros_animais": outros_animais}

    def pega_dados_doador(self):
        print('----------DADOS DOADOR-------------')
        nome = input('Nome: ')
        cpf = input('Cpf: ')
        while True:
            try:
                data_nascimento = input('Data de Nascimento (DD/MM/AAAA): ')
                data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                break
            except ValueError:
                self.mostra_mensagem('Data inválida, insira novamente a data, no formato DD/MM/AAAA. ')
        endereco = input('Endereço: ')
        animal = input('Doar Gato ou Cachorro: ').lower()
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