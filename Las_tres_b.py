import random

precio = []
nombre = []
cantidad = []
total = 0
       
def ingreso():
    cantidad_articulos = int(input("Número de artículos: "))
    if type(cantidad_articulos) == int: #pendiente
        for i in range(cantidad_articulos):
            nombre_articulo = input("Nombre del artículo: ")
            cantidad_vendida = int(input("Cantidad vendida: "))
            if cantidad_vendida >= 1 and cantidad_vendida <= 100:
                cantidad.append(cantidad_vendida)
            else:
                return False
            nombre.append(nombre_articulo)
            precio.append(random.randint(1000, 10000))
    elif cantidad_articulos <= 0 and type(cantidad_articulos) == float():
        print("Error!! Ingrese un numero entero")

def mostrar(total):
    for i1, i2, i3 in zip(nombre, precio, cantidad):
        print("Artículo: " + i1)
        print("Precio: " + "$" + str(i2))
        print("Cantidad: " + str(i3))
    total = sum(precio)
    print("Total a pagar: " + "$" + str(total))

# def total_recaudado():
    
        

menu = """
Bienvenido "Las tres B"

1. Ingresar
2. Mostrar
3. Total recaudado
4. Menos vendido
5. Salir 

Elige una opción: """

opcion = menu
validacion = False

while opcion != 5:
    opcion = int(input(menu))

    if opcion == 1:
        ingreso()
        validacion = True
    elif opcion == 2:
        if validacion == False:
            print("Debe ingresar articulos")
        mostrar(total)



