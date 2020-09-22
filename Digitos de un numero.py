#Escribe el código para leer un número entero x e imprime el número de dígitos de x.
#Por ejemplo, 345 tiene 3 dígitos y 4000 tiene 4 dígitos.

def reto2():
    x = input("Ingresa en numero: ")
    v = len(x)
    print("La cantidad de digitos del numero: ", x, "Es: ",v)

reto2()