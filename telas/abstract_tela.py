class AbstractTela:

    def le_opcao(self, mensagem="", ints_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError 
                return valor_int
            except ValueError: 
                print("Valor inválido")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)    

    def mostra_mensagem(self, msg):
        print(msg)
        print()
    