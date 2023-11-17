"""
            EJERCICIO CON DICCIONARIOS (LIKE OBJECTS IN JS)

            - Names and contact numbers.
            - Actions:
                1. Add/Modify: Browse contact by name, show name and contact;
                    If contact = incorrect => MODIFY?
                    If not found => ADD?
                2. Browse(Coincidence): i.e. Look for: "a" => Displays concidences
                    Use startswith
                3. Delete contact:  Confirm message!!
                4. Show all: Dislays all contact list.
                5. Leave schedule: Close program.
                6. Invalid option, select a valid one.
"""
#Startswith

"""palabra = "Leave schedule: Close program"
verifica = palabra.startswith("Le")
print(verifica)"""

#Diccionarios

"""
Dic = {  }

- Crecen y decrecen
- Se trabaja en función de la clave

Dic = { clave: valor }

"""
"""devices = {
    "Modelo": "Charge 5",
    "SN": "SND6789SDIJ",
    "Warranty status": "ACTIVE",
    "Pairing date": "2023-11-02"
}

dutch = dict(Modelo="Inspire 3", 
             SN="SND67864DIJ", 
             Warranty_status="EXPIRED", 
             Pairing_date="2023-09-02")"""

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

#---------------------------------------------------------------------------------------

contactos = {
    "Nombre":["Jerry Rivera", "Holman Gonzalez", "Jose Manuel"],
    "Teléfono":["3005067789", "3005067789", "3235829969"]
}

print("------------------🤳 Mis contactos 🤳 ------------------\n\n")
print("  |   Nombre   |   Teléfono celular  |  \n")

#Mostrar contactos:
for n, t in zip(range(len(contactos["Nombre"])), range(len(contactos["Teléfono"]))):
    print(f"  |   {contactos['Nombre'][n]}   |   {contactos['Teléfono'][t]}  |  \n\n")
#---------------------------------------------------------------
print("¿Qué desea hacer?:\n")
accion = int(input("Marque el número según sea la acción:\n (1) Para buscar contacto\n (2) Para añadir contacto\n (3) Para eliminar contacto\n\n --- SALIR DE AGENDA: (4) ---\n\n"))
#--------------------------------------------------------------------
if accion == 1:
    busqueda = input("Comience a escribir el nombre y presione enter...")

    print("\nCoincidencias:")
    seleccion = int(input("Seleccione el número correspondiente:\n"))

    coincidencias = []

    for coincide in range(len(contactos["Nombre"])):
        if contactos["Nombre"][coincide].startswith(busqueda) == True:
            #OJO AQUÍ
            
        #No funcional:
        else:
            #OJO AQUÍ
            print("Contacto no encontrado, vuelva a intentar o presione (2) para agregar\n")
            busqueda = input("Comience a escribir el nombre y presione enter...\n")

    for coincide in range(len(coincidencias)):
        print(f"     ({coincide+1})  |   {contactos['Nombre'][coincide]}   |   {contactos['Teléfono'][coincide]}  |  \n") 
   
    
    """Agrega las coincidencia con contacto y nombre a una lista, luego si hay una coincidencia, se aloja en una varibale (Para no tener que usarla en ciclo), se sale del ciclo y se pregunta qué acciones quiere hacer. Si hay más de una coincidencia, muestra el contenido con el indice al frente (indice+1) y de acuerdo al numero marcado (indice-1) se escoge el contacto, se agrega a una variable, se sale del bucle que recorre la lista con las coincidencias y se pregunta la acción"
        
        

    """print("¿Qué desea hacer con este contacto?:\n")
    accion_contacto = int(input("Marque el número según sea la acción:\n (1) Para modificar contacto\n (2) Para eliminar contacto\n\n --- SALIR DE AGENDA: (4) ---\n\n"))

elif accion == 2: 
    print("+ Añadiendo nuevo contacto... 👭👬 +\n")
    agregar_nombre = input("Ingrese el nombre del contacto: ")
    agregar_numero = input(f"Ingrese el numero de contacto de {agregar_nombre}: ")

    contactos["Nombre"].append(agregar_nombre)
    contactos["Teléfono"].append(agregar_numero)
    
    print("\n Sistema: Contacto agregado exitosamente 👍\n")

    #Desea agregar otro o salir??

    print("------------------🤳 Nuevos contactos 🤳 ------------------\n\n")
    print(f"  |   {contactos['Nombre'][-1]}   |   {contactos['Teléfono'][-1]}  |  \n")

elif accion == 3:
    print(" ⚠ ELiminar contacto ⚠\n")

    #Falta


def nombre_funcion(argumentos):
    código
    return retorno"""