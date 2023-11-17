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
def Buscar_Contacto():

        busqueda = input("Comience a escribir el nombre y presione enter...")

        print(f"\nCoincidencias:")

        coincidencias = {
            "Name":[],
            "Number":[]
        }

        for coincide in range(len(contactos["Nombre"])):
            if contactos["Nombre"][coincide].startswith(busqueda):
                coincidencias["Name"].append(contactos["Nombre"][coincide])
                coincidencias["Number"].append(contactos["Teléfono"][coincide])
        

        if int(len(coincidencias["Name"])) > 0:
            for a in range(len(coincidencias["Name"])):
                print(f'     ({a+1})  |   {coincidencias["Name"][a]}   |   {coincidencias["Number"][a]}  |  \n') 
        else:
            print("No se encontraron coincidencias.")
        """else: 
            print("Contacto no encontrado, vuelva a intentar o presione (2) para agregar\n")
            busqueda = input("Comience a escribir el nombre y presione enter...\n")"""
        seleccion = int(input(f"-- Seleccione el número correspondiente --\n"))

        #Se recorre la lista Name en Concidencias
        for a in range(len(coincidencias["Name"])):
                #Si el número del contacto que se quiere modificar coincide con uno de los índices de la lista de coincidencias entonces:
                if a == (seleccion-1):
                    #Se recorre la agenda (diccionario principal) contactos.
                    for b in contactos["Nombre"]:
                        #Si el valor del nombre seleccionado en lista name de coincidencias hace match con un valor de la lista Nombre en contactos:
                        if coincidencias["Name"][a] == b:
                            #Se comprueba la existencia del valor (b) en la lista Nombre de contactos:
                            if b in contactos["Nombre"]: 
                                #Se guarda el índice de tal valor en una variable, si existe:
                                index_b = contactos["Nombre"].index(b)
        return index_b

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Modificar_contacto(Index):
            #Se ingresan valores que van a remplazar los actuales en listas Nombre y Teléfono con el mismo índice (index_b)
            nombre_mod = input(f"Nombre actual: {contactos['Nombre'][Index]}\n Digite el nuevo nombre:")
            contactos["Nombre"][Index] = nombre_mod
                                
            numero_mod = input(f"\nNúmero de contacto actual: {contactos['Teléfono'][Index]}\n Digite el nuevo número:")
            contactos["Teléfono"][Index] = numero_mod                  

            #Se imprime de nuevo la lista de contactos
            print(f"------------------🤳 Mis contactos 🤳 ------------------\n\n")
            print(f"  |   Nombre   |   Teléfono celular  |  \n")

            for n, t in zip(range(len(contactos["Nombre"])), range(len(contactos["Teléfono"]))):
                print(f"  |   {contactos['Nombre'][n]}   |   {contactos['Teléfono'][t]}  |  \n\n")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Eliminar_contacto(Index):
            contactos["Nombre"].pop(Index)
            contactos["Teléfono"].pop(Index)

            print(f"------------------🤳 Mis contactos 🤳 ------------------\n\n")
            print(f"  |   Nombre   |   Teléfono celular  |  \n")

            for n, t in zip(range(len(contactos["Nombre"])), range(len(contactos["Teléfono"]))):
                print(f"  |   {contactos['Nombre'][n]}   |   {contactos['Teléfono'][t]}  |  \n\n")   

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Agregar_Contacto():

        print("+ Añadiendo nuevo contacto... 👭👬 +\n")
        agregar_nombre = input("Ingrese el nombre del contacto: ")
        agregar_numero = input(f"Ingrese el numero de contacto de {agregar_nombre}: ")

        contactos["Nombre"].append(agregar_nombre)
        contactos["Teléfono"].append(agregar_numero)
        
        print("\n Sistema: Contacto agregado exitosamente 👍\n")


        print(f"------------------🤳 Nuevos contactos 🤳 ------------------\n\n")
        print(f"  |   {contactos['Nombre'][-1]}   |   {contactos['Teléfono'][-1]}  |  \n\n")

        print(f"------------------🤳 Mis contactos 🤳 ------------------\n\n")
        print(f"  |   Nombre   |   Teléfono celular  |  \n")

        for n, t in zip(range(len(contactos["Nombre"])), range(len(contactos["Teléfono"]))):
            print(f"  |   {contactos['Nombre'][n]}   |   {contactos['Teléfono'][t]}  |  \n\n")

 ######################################## AGENDA ############################################
contactos = {
                "Nombre":["Jerry Rivera", "Holman Gonzalez", "Jose Manuel"],
                "Teléfono":["3005067789", "3005067789", "3235829969"]
            }

print("------------------🤳 Mis contactos 🤳 ------------------\n\n")
print("  |   Nombre   |   Teléfono celular  |  \n")

#Mostrar contactos al iniciar:
for n, t in zip(range(len(contactos["Nombre"])), range(len(contactos["Teléfono"]))):
    print(f"  |   {contactos['Nombre'][n]}   |   {contactos['Teléfono'][t]}  |  \n\n")

############################################################################################## 
#---------------- INICIO DE LA AGENDA FUNCIONAL -----------------------------------------------

continuar = input(f"¿Desea acceder a la agenda?\n Marque 's', de lo contrario presione Enter\n")

while continuar == "s":

    print("¿Qué desea hacer?:\n")
    accion = int(input(f"Marque el número según sea la acción:\n (1) Para buscar contacto\n (2) Para añadir contacto\n (3) Para eliminar contacto\n\n ---\n\n"))
    #--------------------------------------------------------------------
    if accion == 1:
        #Se debe crear una variable donde se va a alojar lo que la función retorne
        Contacto_Buscar = Buscar_Contacto()

        print(f"¿Qué desea hacer con el contacto seleccionado?:\n")
        accion_contacto = int(input(f"Marque el número según sea la acción:\n (1) Para modificar contacto\n (2) Para eliminar contacto\n\n"))
        
        if accion_contacto == 1:
            print(f"+ 🖊🖊 Modificando contacto... 🖊🖊 +\n")
        
            #La función buscar contacto le retorna el índice del nombre en la lista principal          
            Modificar_contacto(Contacto_Buscar)

        elif accion_contacto == 2:
            print(F"- ⚠ Eliminando contacto ⚠ -\n")                        

            #La función buscar contacto le retorna el índice del nombre en la lista principal          
            Eliminar_contacto(Contacto_Buscar)
            

    elif accion == 2:      
        Agregar_Contacto()

    elif accion == 3:
        Contacto_Eliminar =  Buscar_Contacto()
        Eliminar_contacto(Contacto_Eliminar)

    continuar = input(f"¿Desea continuar en la agenda?\n Marque 's', de lo contrario presione Enter")
    

    
