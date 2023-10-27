suma = int(input("Primer valor #"))

numero = input("Ingrese numero No. 2\n")
    
num = int(numero)

operando = input("Ingrese operando\n")

contador = 0

"""numero0 = input("Ingrese el primer multiplicando\n")
"""
while True:


    """if contador == 0:
         suma = int(numero0)"""


    if operando == "*":

        suma = int(suma * num)

    elif operando == "/":
        
        suma = int(suma / num)

    elif numero == "" or operando == "":
            break  
    
    numero = input(f"Ingrese numero {contador+3}\n")
    
    num = int(numero)

    operando = input("Ingrese operando {contador}\n")
    
    contador += 1
    
print(f"resultado = {suma}")

        