
numero = int(input("Escribe un numero: "))

def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    return contador

if es_primo(numero) != 2 :
    print("No es primo")
else:
    print("Es primo")

    




