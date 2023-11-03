"""
1. Escriba un programa que solicite al usuario el año actual y otro año cualquiera, este debe mostrar en un mensaje claro para el usuario cuantos años han pasado o faltan para llegar a ese año. """



"""
2. Realizar un programa que muestre un menú con opciones de colores primario (Amarillo, azul, rojo, blanco y negro), el usuario debe escoger 2 colores de los ofrecidos en el menú y con una secuencia de if y elif evaluar las posibles combinaciones generadas con los colores primarios. Si el usuario escogió colores que no generan debe mostrar un mensaje que indique que no existe combinación posible"""


"""
3. Escribir un programa que calcule el área de las siguientes figuras: triangulo, circulo, cuadrado y rectángulo, el usuario debe escoger la figura a la que desea calcular el área.
Debe mostrar mensaje que indique los parámetros utilizados para calcular el área y el resultado de la operación.


4. Solicitar al usuario 4 números, el programa debe mostrar si hay un numero repetido al menos 2 veces, si todos son diferentes o todos son iguales
"""
print("A continuación, va a ingresar cuatro (4) digitos, si cumple con las condición, lo sabrá:")

clave = int(input("Ingrese un digito\n"))
clave2 = int(input("Ingrese otro digito\n"))
clave3 = int(input("Ingrese un 3er digito\n"))
clave4 = int(input("Ingrese un 4to digito\n"))

if clave == clave2 == clave3 or clave2 == clave3 == clave4 or clave == clave2 == clave4 or clave == clave3 == clave4:
    print("Hay 3 digitos iguales")
elif clave == clave2 and clave2 == clave3 and clave3 == clave4:
    print("Todos los digitos iguales")
elif clave == clave2 or clave == clave3 or clave == clave4:
    print("Hay dos digitos iguales")
elif clave2 == clave3 or clave2 == clave3:
    print("Hay dos digitos iguales y dos diferentes")
elif clave3 == clave4:
    print("Hay dos digitos iguales")
else:
    print("Todos los digitos son diferentes")

clave = []

for num in range(4):
    clave.append(int(input(f"Ingrese el digito Nro.{num}  ")))

numComp = 0

for inputN in range(len(clave)):
    if clave[inputN] == clave[0]:
        numComp += 1
    else:
        numComp = numComp - 1

if  numComp == 4:
            print("Todos los digitos iguales")
elif numComp == 0:
            print("Hay dos digitos iguales")
elif numComp < 4 or numComp > 0 or numComp < 0 and numComp > -4:
            print("Hay 3 digitos iguales")
else:
            print("Todos los digitos son diferentes")

"""
IF – ELSE:

1. Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 2.500.000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
2. Solicitar un numero por teclado y mostrar en pantalla si es un numero primo o no"""