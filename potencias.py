def potencia():
    LIMITE = 1000
    contador = 0
    resultado = 2 ** contador
    while resultado < LIMITE:
        print("2 elevado a " + str(contador) + " = " + str(resultado))
        contador = contador + 1
        resultado = 2 ** contador


if __name__ == '__main__':
    potencia()