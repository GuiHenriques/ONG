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
        nome = input('Insira seu nome: ')
        cpf = input('Insira seu cpf: ')
        dia = input('Insira o dia em que nasceu: ')
        mes = input('Insira o mês em que nasceu: ')
        ano = input('Insira o ano em que nasceu: ')
        endereco = input('Insira o seu endereço: ')
        data_nascimento = list()
        data_nascimento.append(dia)
        data_nascimento.append(mes)
        data_nascimento.append(ano)
        #duas opcoes: pegar input do dia, mes e ano e depois juntar tudo, OU usar um unico input no formato dd/mm/aaaa.
        #beneficio de ser separado seria o tratamento de casos em que a pessoa n é maior de 18.
        '''
        from datetime import date, datetime

        data = datetime.strptime('26/08/2018', '%d/%m/%Y').date()

        print(data)

        dataFormatada = data.strftime('%d/%m/%Y')

        print(dataFormatada)
        '''                      

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
        
        
        
    
    def mostra_mensagem(self,msg):
        print(msg)