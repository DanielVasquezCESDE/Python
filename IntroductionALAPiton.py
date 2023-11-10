
#https://www.programiz.com/python-programming/keywords-identifier


"""residence_country = "Canada"
print(type(residence_country))

if residence_country == "Canada":
    print("Thanks for letting me know")
else: 
    print("Thanks, I appreciate your colaboration")

n1 = 23
n2 = 2.4
resultado = n2 + n1

print("Concat works like this: ", residence_country)
#La f abajo habilita un uso parecido al Template Literals en JS
print(f"El resultado de sumar {n1} con {n2} es {resultado}")
print("El resultado de sumar " + str(n1) + " con "+ str(n2) + " es resultado")

division_Decimal = n1 / n2
division_Entera = n2 // n1

powered_potenciacion = n1 ** n2
raizCuadrada = n1 ** 0.5
#Residuo
mod = n1 % n2

#Datos de entrada
#Request the user to input a interger number
valor = int(input("Input the 4-digit setup code screening on your Fitbit, please. It's not necessary include the middle hashes ¯\_(ツ)_/¯"))

if valor == true and valor > 4:
    raizC = valor ** 0.5
    print(f"Setup process succeed, process id: {raizC}")
else:
    print(f"Setup process failed, error id: {raizC}")"""


"""Calcular el valor de parqueadero. Pedir la info. que se considere 

Customer_Name = input("Ingrese nombre del usuario")
Tipo_Vehiculo = input("Ingrese el tipo de vehiculo: 'm' para motocicletas y 'c' para carros")
Hora_Entrada = int(input("Ingrese hora de entrada (Formato de 24h, sin incluir minutos)"))
Hora_Salida = int(input("Ingrese hora de salida (Formato de 24h, sin incluir minutos)"))

CostoHoraMoto = 2000
CostoHoraCarro = 4000"""

"""
dolly 70g $43000
clown 95g $57000
Calcular precio total y peso del encargo
¿Cuantos y de cuáles a comprar?"""

#Determinar si el valor del número entered is a positive interger and if It's par or impar

"""
ELIF: 

if condition:
    instruction1
elif condition2:
    instruction2
elif condition3:
    instruction3
else: 
    instruction(last)
    """

#Mostrar mensaje según tipo de mascota ingresada
#pet_User = int(input("Please, tell us which of the next type of animal your pet is:\n \t1. "dog"\t2. "cat"\t3. "fish"\t4. "parrot" \t5. "None of the previous"Note: Input the corresponding number\n")) 
"""
if pet_User == 1:
    print("Mostrame una foto de ese chandoso, querido tuyo")
elif pet_User == 2:
    print("¿Y no suelta mucho pelo?, ¿Es gata?, ¿Ya la operó?")
elif pet_User == 3:
    print("¿De cuáles tiene? ¿Solitarios?, ¿No se le han enfermado?")
elif pet_User == 4:
    print("Nando!, Nando!, Ama...!, ¡Y hable y hable!")
elif pet_User == 5:
    print("Don't you want acompanion? Something to take care about?")"""

#Diferencia entre fechas (años)
#Usuario escoge dos colores de Amarillo, azul, rojo, blanco, y negro. Mostrar combinación
#Calcular área de figura escogida: circulo, triángulo, rectángulo, etc.
#Usuario ingresa 4 números: mostrar si todos son iguales, al menos 2 iguales o si son diferentes.


"""print("A continuación, va a ingresar cuatro (4) digitos, si cumple con las condición, lo sabrá:")

clave = int(input("Ingrese un digito"))
clave2 = int(input("Ingrese otro digito"))
clave3 = int(input("Ingrese un 3er digito"))
clave4 = int(input("Ingrese un 4to digito"))

if clave == clave2 and clave2 == clave3 and clave3 == clave4:
    print("Todos los digitos iguales")
elif clave == clave2 or clave == clave3 or clave == clave4:
    print("Hay dos digitos iguales")
elif clave2 == clave3 or clave2 == clave3:
    print("Hay dos digitos iguales")
elif clave3 == clave4:
    print("Hay dos digitos iguales")
else:
    print("Todos los digitos son diferentes")"""

"""clave = []

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
            print("Todos los digitos son diferentes")"""



"""
Iterar listas
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

Iterar listas con rango
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])"""

#--------------------------------------------------------------------------------------------------

#                                                       While loop

#Numbers 1 to 10

"""
# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 10

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1"""

"""
#Numeros pares < 20

number = int(input("Input a deadline for the countdown:\n"))

i = 0
number_str = ""

while i <= number:
    if i % 2 == 0:
        number_str += f"{str(i)}, "
    i += 1

print(f"Even numbers 'til {number}: {number_str}\n")"""


"""
#Access 4-digit pin, unless it matches with an specific pin no access given. 

rec_pin = 2344

limit = 0
i = 2

access = False

while i >= limit and access != True:
    user_pin = int(input(f"Enter your 4-digit pin\n ({int(i+1)} attempt(s) remaining)\n"))

    if user_pin == rec_pin:
        access = True
        i -= 1
        print("Welcome!")
    else: 
      i -= 1
      print("Wrong pin")

if access == False:
        print("You ran out of attempts!")"""



#Calculate geometrical figures areas until User inputs 6

"""
#While else:
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

#Break
# program to find first 5 multiples of 6

i = 1

while i <= 10:
    print('6 * ',(i), '=',6 * i)

    if i >= 5:
        break
    
    i = i + 1"""

#-----------------------------------------------------------------------------------
"""Write a function in Python that accepts a credit card number. It should return a string 
    where all the characters are hidden with an asterisk except the last four. 
    For example, if the function gets sent “4444444444444444”, then it should return “4444”."""

  
"""card_number = int(input("Input your card number"))

while card_number != 12 or type(card_number) != int:
    card_number = int(input("Please, input a correct card number format"))

print("Let's move on")"""



"""
#Strings could be considered as character lists

text = "Welcome!"
for letter in text:
    print(letter)

#Check and count the 'e' vowel within a string:

text = "Welcome"
quantity = 0
for index in range(len(text)):
    if text[index] == 'e':
        quantity += 1
print(f"Word '{text}' contains {quantity} times vowel 'e'")
"""

#--------------------------------------------------------
#                    2023-10-19 - COLECCIONES
#Collection

#Listas, tuplas y diccionarios

#1.Listas 

"""
Condición no conocida: Sólo puede contener un tipo de valor

Métodos:
    1. append()
    2. insert(index, element)
    3. pop() (se indica index)
    4. remove() (Se indica elemento)
        - Ascendente:
    5. sort()
        - De forma descendente
    6. sort(reverse = True)
    7. index() (Devuelve posición de elemento)
    8. count() 
    9. len()
"""

"""common_issues = ["Charge 6 delayed order", "Charge 5 Battery", "Body responses"]

#Se puede recorrer al revés, de derecha a izquierda usando valores negativos
print(common_issues[-1]) #Muestra Body responses

common_issues[2] = "Steps tracking units discrepancy"

#Las tuplas almacenan datos que nose editan
"""

#------------------------------------------------------------------------------------------------------------------------

#2023-10-26

#Remover elementos de las listas

"""
1. lista.pop() => Elimina elemento por índice
2. lista.remove() => Elimina elemento por llave
3. clear() => Elimina 


numbers = [1,32,543,-234,2,45,66789,-4231,12,-32,0,8,23,45]
oddnegative = []

for n in numbers:
    if n % 2 != 0 or n < 0:
        oddnegative.append(n)
        
print(oddnegative)"""
    
#------------------------------------------------------------------------------------------------------------------------

#2023-11-02

#Tuplas

"""
Inmutable = false

Representación
    tuplas = ()

De un elemento:
    tupla = elemento,   //La coma defina que es una tupla y no una variable sola.

De varios elementos:
    tupla = elemento1, elemento2, elemento3,
De varios elementos con paréntesis:
    tupla = (elemento1, elemento2, elemento3)

Not compatible methods:
    1. pop()
    2. insert()
    3. remove()
    4. sort()
    5. append()

"""

"""devices = "Charge 5", "Versa 3", "Sense", "Ionic"
print(type(devices))

#Access to an element
issues = "Battery not charging", "Display corrupted", "Sleep tracking", "Refund for recall"
print(issues[3])"""

#Contar cuántas veces se repite un dato específico

"""horas_clave = "5:58", "7:48", "10:50", "13:40", "14:00", "14:00"

print(f"Las 14:00 horas programadas, se repiten {horas_clave.count('14:00')} veces")"""

#Concatenar tuplas:
"""horas_clave = "5:58", "7:48", "10:50", "13:40", "14:00", "14:00"
issues = "Battery not charging", "Display corrupted", "Sleep tracking", "Refund for recall"
devices = "Charge 5", "Versa 3", "Sense", "Ionic" 

merged_tuple = issues + devices
print(merged_tuple)"""

#Concatenar convirtiendo y ordenando tuplas 
"""horas_clave = "5:58", "7:48", "10:50", "13:40", "14:00", "14:00"
issues = "Battery not charging", "Display corrupted", "Sleep tracking", "Refund for recall"
devices = "Charge 5", "Versa 3", "Sense", "Ionic"

list_comb = list(horas_clave) + list(issues)

list_comb.sort()

for i in list_comb:
    print(list_comb)
    break"""

#-----------------------------------------------------------------------------------------------------------

#Diccionarios

"""
Dic = {  }

- Crecen y decrecen
- Se trabaja en función de la clave

Dic = { clave: valor }

"""
devices = {
    "Modelo": "Charge 5",
    "SN": "SND6789SDIJ",
    "Warranty status": "ACTIVE",
    "Pairing date": "2023-11-02"
}

dutch = dict(Modelo="Inspire 3", 
             SN="SND67864DIJ", 
             Warranty_status="EXPIRED", 
             Pairing_date="2023-09-02")

#Access to an element

"""print(devices[SN])"""

#Access to element by using .get()

"""print(devices.get("Warranty status"))"""

#Modificar un valor de la clave:

"""devices[SN] = "NFI78987FD8"""

#Modificar un elemento (clave) que no existe:

"""devices["Pairing date"] = "2022-09-09"""

#Acceder a las claves sin usar el método .key()

"""for clave in devices:
    print(clave)"""

#Acceder a los valores del diciconario sin el método .values()

"""for valor in devices:
    print(devices[valor])"""

#Obtener clave y valor con el método .items()

"""for clave, valor in devices.items():
    print(f"{clave} = {valor}")"""

#pop() ---> dedelete an specific item, the argument is the key, popitem() ---> deletes the last item in a dictionary, clear() --> Erases all items within the dict

