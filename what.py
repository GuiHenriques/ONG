vacinas_validas = ["Raiva", "Leptospirose", "Hepatite Infecciosa"]
while True:
    tipo = input("Tipo: ").capitalize()
    if tipo in vacinas_validas:
        break
    else:
        print("Tipo inválido")
print("Vacina adicionada com sucesso")