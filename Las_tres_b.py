import random

precio = []
nombre = []
cantidad = []

       
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

    # print(nombre, precio, cantidad)
    # return nombre, precio, cantidad

def mostrar():
    # ingreso()
    return print(nombre, precio, cantidad)
    # return sum(precio)
        
    


menu = """
Bienvenido "Las tres B"

1. Ingresar
2. Mostrar
3. Total recaudado
4. Menos vendido
5. Salir 

Elige una opción: """

opcion = int(input(menu))

# contador = 1
# # def run():
# #     if opcion == 1:
# #         ingreso()
# #         print(int(input(menu)))
# #     elif opcion == 2:
# #         if opcion == 1:
            
# #         mostrar()


# # if __name__ == '__main__':
# #     run()
  
# while opcion <= 5:
#     opcion = int(input(menu))
#     if opcion == 1:
#         ingreso()
#     # elif opcion == 2:
#     #     print("hola")   

if opcion == 1:
    ingreso()
elif opcion == 2:
    print(nombre)