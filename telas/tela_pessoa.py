class TelaPessoa():
    #area para tratamento de dados
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