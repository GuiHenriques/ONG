from datetime import date,datetime
class TelaPessoa():
    #area para tratamento de dados
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError #será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError: #aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

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
    
        opcao = int(input("Escolha uma opcao: "))
        return opcao
    
    def pega_dados_adotante(self):
        print('------------------------')
        nome = input('Insira seu nome: ')
        cpf = input('Insira seu cpf: ')
        data_nascimento = input('Insira sua data de nascimento no formato DD/MM/AAAA: ')
        endereco = input('Insira o seu endereço: ')
        tipo_hab = input('Insira o tipo da sua habitacao: casa ou apartamento ')
        tam_hab = input('Insira o tamanho da sua habitacao: p, m ou g ')
        outros_animais = input('Possui outros animais? Responda com "sim" ou "nao" ')
        data_f = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        #o tratamento da idade caso seja menor de idade:
        today = date.today()
        age = today.year - data_f.year - ((today.month, today.day) < (data_f.month, data_f.day))
        #if age < 18:
            #raise alguma exception.Finalizar o programa ou pedir a data de novo?
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_f, "endereco": endereco,"tipo_hab": tipo_hab, "tam_hab": tam_hab, "outros_animais": outros_animais}
        
    def mostra_adotante(self,dados_adotante):
        print('----------------------------')
        print('Nome: ', dados_adotante['nome'])
        print('Cpf : ', dados_adotante['cpf'])
        print('Data de nascimento: ', dados_adotante['data_nascimento'])
        print('Endereco: ', dados_adotante['endereco'])
        print('Tipo de habitacao: ', dados_adotante['tipo_hab'])
        print('Tamanho da habitacao: ', dados_adotante['tam_hab'])
        print('Possui outros animais: ', dados_adotante['outros_animais'])
        print("\n")

    def pega_cpf(self):
        cpf = input('Insira o cpf da pessoa: ')
        return cpf
    
    def mostra_mensagem(self,msg):
        print(msg)