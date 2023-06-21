from telas.abstract_tela import AbstractTela
from datetime import date, datetime


class TelaPessoa(AbstractTela):

    def tela_opcoes(self, tipo):
        print(f"-------- {tipo} ----------")
        print("Escolha a opcao")
        print(f"1 - Incluir {tipo}")
        print(f"2 - Alterar {tipo}")
        print(f"3 - Listar {tipo}s") if tipo == 'Adotante' else print(f"3 - Listar {tipo}es")
        print(f"4 - Excluir {tipo}")
        print("0 - Retornar")

        opcao = self.le_opcao("Escolha uma opcao: ", [0, 1, 2, 3, 4])
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

    def seleciona_tipo_pessoa(self):
        print("-------- Pessoa ----------")
        print("1 - Adotante")
        print("2 - Doador")
        print("0 - Retornar")

        tipo = self.le_opcao("Escolha a opção: ", [0, 1, 2])
        if tipo == 0: return None

        animal = "Adotante" if tipo == 1 else "Doador"
        return animal

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