class TelaSistema():

    #essa função trata o caso de não digitar um valor valido
    #note que está dentro de um while True. Só sai do loop quando digitado um valor correto
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
        print("-------- PREENCHER ---------")
        print("Escolha sua opcao")
        print("1 - Realizar doação")
        print("2 - Realizar adoção")
        print("3 - Gerenciar pessoas")
        print("4 - Sei la")
        print("0 - Finalizar Sistema")
        opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4])
        return opcao
TelaSistema().tela_opcoes()