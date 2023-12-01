"""

            1. Crea Función Calcular Max y Min: recibe una lista de enteros y
            devuelve el máximo y el mínimo de los números guardados en la
            lista.
            Parámetros de entrada: lista de enteros
            Valores de salida: valor máximo y mínimo. 
            
                        2. Usa la función MaxMin que recibe una lista con valores
            numéricos y devuelve el valor máximo y el mínimo creada
            anteriormente y crea un programa que pida números por teclado
            y muestre el máximo y el mínimo, utilizando la función anterior. """

"""enteros = []

agregar = int(input("¿Cuántos valores desea agregar?: "))

for i in range(agregar):
    num = int(input(f"Valor Nro. {i+1}:  "))
    enteros.append(num)

def Mostrar_Mayor (lista):
    n = lista[0]
    for x in range(len(lista)):
        if n < lista[x]:
            n = lista[x]
    print(f"Valor mayor: {n}")

def Mostrar_Menor (lista):
    n = lista[0]
    for x in range(len(lista)):
        if n > lista[x]:
            n = lista[x]
    print(f"Valor menor: {n}")

Mostrar_Mayor(enteros)
Mostrar_Menor(enteros)"""


"""            3. Solicitar al usuario que ingrese su dirección email. Imprimir un
            mensaje indicando si la dirección es válida o no, valiéndose de
            una función para decidirlo. Una dirección se considerará válida si
            contiene el símbolo "@". """



"""email = input("Ingrese su dirección de correo eléctrónico:\n")

def Validar_Correo (e):
    valido = False
    for index in range(len(e)):
        if e[index] == '@':
            valido = True
        else:
            valido == False
    if (valido == True):
        print(f"\n El correo {email} es válido\n")
    else: 
        print(f"\n El correo {email} no es válido, intente de nuevo.\n")
        email2 = input("Intente de nuevo, verifque el correo:\n")
        Validar_Correo(email2)

Validar_Correo(email)"""




"""            4. Requerir al usuario que ingrese un número entero e informar si
            es primo o no, utilizando una función booleana que lo decida. """

"""numb = int(input("Ingrese el número a comprobar: "))


def Validar_Primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

Validar_Primo(numb)"""


"""            5. Escribir una función que reciba una muestra de números en una
            lista y devuelva otra lista con sus cubos, es decir, el número
            elevado a la 3.

"""

"""enteros = []

agregar = int(input("¿Cuántos valores desea agregar?: "))

for i in range(agregar):
    num = int(input(f"Valor Nro. {i+1}:  "))
    enteros.append(num)

def Mostrar_Valores_al_Cubo (lista):
    lista_cubos = []
    for a in lista:
        cubo = a**3
        lista_cubos.append(cubo)
    return lista_cubos


Cubos = Mostrar_Valores_al_Cubo(enteros)

print(f" Valores al cubo \n")
for n in range(len(enteros)):
    print(f" {enteros[n]} ^ 3 = {Cubos[n]}")"""