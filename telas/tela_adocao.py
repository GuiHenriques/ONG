class TelaAdocao():

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
        print("-------- Adocao ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adocao")
        print("2 - Alterar Adocao")
        print("3 - Listar Adocoes")
        print("4 - Excluir Adocao")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4])
        return opcao
