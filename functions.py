#Pythons Functions
# - Traditional ones

"""def nombre_funcion(argumentos):
    código
    return 
"""
# - Lambda functions

    #Función sin argumentos y sin retono

"""def saludo():
    print("que aburridora la clase güevón, tomale fotos a lo que llevamos y abrámonos")

texto = saludo()
print(texto)"""


    #Función con argumentos y sin retorno

"""def nomi(tier_1):
    print(f"Que más {tier_1}")

ask = input("Ingrese elnombre del tier 1:\n")
nomi(ask)"""

""" Calcular promedio de dos notas"""

"""def promedio(numb):
    ave = (numb + numb)/2
    return ave


ask = int(input("Ingrese el Nro. 1:\n"))

promedio(ask)"""

#Dunciones con valores predeterminados

"""def multi(a, b=3, c=4):
    return a*b*c
print(multi(2, 5)) #Por más que se le asigne un valor al parámetro, la prioridad es la del valor que se le ingrese (input)"""

"""def sum(d, e, f):
    result = d+e+f
    return result

print(sum(12, 456, 10000))"""

#Parámetros de longitud variable:

"""def multiply(*num):
    result = 0
    for i in num:
        result *= i

print(multiply(3,5,4,3)) """#El asterisco se usa para indicar un número indeterminado de parámetros

#Filtrar de lista sólo los impares

"""def Filtrar_Impar(lista):
    impares = []
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            impares.append(lista[i])
    print(impares)

numeros = [34, 35, 36, 37, 38, 39, 40, 41]

print(Filtrar_Impar(numeros))"""

#Lambda

numeros = [34, 35, 36, 37, 38, 39, 40, 41]

nueva_lista = filter(lambda x: x%2 != 0, numeros)
print(list(nueva_lista))