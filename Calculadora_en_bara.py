"""EJERCICIO WHILE
Hacer una calculadora en Python usando el ciclo while, teniendo en cuenta lo siguiente:
- El usuario debe ingresar los datos a tener en cuenta en las operaciones.
- La calculadora debe contener las siguientes opciones:
o Suma
o Resta
o Multiplicación
o División: para realizar esta operación debe tener una restricción que evite que el
usuario ingrese 0 como divisor.




o Potenciación
o Factorial de un numero ingresado
o Raíz cuadrada, debe especificar que el dato a ingresar debe ser entero positivo
o Cambiar números
o Salir
- Crear un código que arroje el resultado de la operación escogida por el usuario.
Para la calculadora puede importar la librería math (import math) y utilizar las siguientes funciones:
Math.sqrt(número): calcular raíz cuadrada de cualquier numero
Math.isqrt(numero): calcular raíz cuadrada. Arroja resultado int
Pow(a, b): utilizada para potenciación donde a es el numero base y b seria el exponente.
Math.factorial(n): calcula el factorial."""

import math

print("Seleccione qué operación desea realizar\n (1). Suma\n (2). Resta\n (3). Multiplicación\n (4). División\n (5). Potenciación\n (6). Factorial\n (7). Raíz cuadrada\n (8). SALIR\n")

opcion = int(input(">"))

if (opcion): 

    if (opcion == 1 ):

        print("Ingrese los números a sumar y/o restar (Para restar, agregue el signo '-' antes del signo), para terminar de agregar, presione ENTER") 

        i = 0

        operandos = 0  # Inicializa sumandos a 0

        while True:
            entrada = input(f"Valor {i+1} (o presione ENTER para finalizar): ")
            if entrada == "":
                break  # Sale del bucle si el usuario presiona ENTER
            else:
                numero = float(entrada)  # Convierte la entrada a un número de punto flotante
                
                operandos += numero  # Suma el número a los sumandos

                i += 1

        print(f"El resultado de la operación es: {operandos}")

    if (opcion == 2):

        print("Ingrese los números a multiplicar y/o dividir, para terminar de agregar, presione ENTER") 

        i = 0

        operandos2 = 0  

        while True:
            entrada = input(f"Valor {i+1} (o presione ENTER para finalizar): ")
            if entrada == "":
                break  

            else:

                if type (entrada) == int or type (entrada) == float:
                    numero = float(entrada)  

                
                    if entrada == '*':

                        multi = numero * operandos2 

                        operandos2 += multi

                    elif entrada == '/':

                        divid = numero / operandos2

                        operandos2 += divid

                    else:

                        operandos2 += numero

                i += 1

        print(f"El resultado de la operación es: {operandos2}")







    


