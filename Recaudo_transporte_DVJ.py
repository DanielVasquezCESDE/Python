
"""Una empresa llamada “Transportes Cesde” requiere guardar los nombres de los
conductores y el dineroque recaudan cada día de la semana (lun a sábado)
movilizando a la comunidad educativa 
y el porcentaje de recaudo de cada conductor.
Para guardar esta información se crearán las siguientes listas:

NombreConductor: para almacenar los nombres de los conductores.

DiasSemana: que contiene los días de lunes a sábado.

Recaudo: lista para guardar la cantidad recolectada cada día de la semana.

Se debe generar una lista llamada total recaudo con la suma total de lo recaudado
por cada conductor.

Debe solicitar el número de conductores que hacen parte de la empresa de
Transporte Cesde.
"""

dias_Semana = ("Lunes", "Martes", "Miércoles", "Jueves", "viernes", "Sábado", "Domingo")

print("-------------------------- TRANSPORTES CESDE -------------------------- \n\n")
cantidad_conductores = int(input("Ingrese la cantidad de conductores de los que se registra el recaudo bruto:\n"))

nombre_conductor = []
#LISTA BIDIMENSIONAL, que almacena los recaudos, primero por día y luego por codnuctor.
recaudo_semanal = []

#Lista que acumula los recaudos totales a la semana por conductor
semana_conductor = []

porcentaje_recaudo = []

for nombre in range(cantidad_conductores):
    nombre_conductor.append(input(f"Ingrese el nombre del conductor Nro. {nombre+1}\n"))

for dia in range(len(dias_Semana)):
    #Se inicia la lista que tiene guardados los acumulados por conductor, esto, cada vez que se cambia de día
    recaudo_dia_conductor = []
    print(f"Ingrese el recaudo registrado para el {dias_Semana[dia]}:\n")

    for driver in range(cantidad_conductores):
        print(f"                   Conductor(a): {nombre_conductor[driver]}         ")
        recaudo_dia_conductor.append(float(input(f"Ingrese el dinero total recaudado para el {dias_Semana[dia]}, por {nombre_conductor[driver]} en pesos:\n$")))
        print("-------------------------------------------------------------")
    #Se agrega la lista de acumulados por conductor por día a la lista general de la semana.
    recaudo_semanal.append(recaudo_dia_conductor)
    print("################################################################################")

#Variable acumuladora de los recaudos totales (general)
total_semana = 0

for c in range(cantidad_conductores):
    #Se reinicia la variable acumuladora del recaudo semanal total por conductor, esto, cuando se pasa al siguiente.
    acumula = 0
    for d in range(len(dias_Semana)):
        acumula += recaudo_semanal[d][c]
    #Se agregan los totales semanales por conductor a la lista semana_conductor
    semana_conductor.append(acumula)
    #Se suman todos los totales semanales de los conductores para el total general.
    total_semana += semana_conductor[c]


for c in range(cantidad_conductores):
    #Se calcula el porcentaje de recaudo semanal general por cada conductor
    porcentaje_recaudo.append((semana_conductor[c]*100)/total_semana)

#--------------------------------- Se muestran los resultados ---------------------------------

for day in range(len(dias_Semana)):
    print(f"------------------- {dias_Semana[day]} -------------------\n")
    for conductor in range(cantidad_conductores):
        print(f"                     Conductor(a): {nombre_conductor[conductor]}             \n")
        print(f"Recaudo del {dias_Semana[day]}: ${recaudo_semanal[day][conductor]} pesos.\n")
    print(f" ******************* Recaudo total del día: ${sum(recaudo_semanal[day])}pesos *******************\n")

print("------------------------------------ TOTAL DE RECAUDOS A LA SEMANA ------------------------------------\n")

for c in range(cantidad_conductores):
    print(f"El total recaudado por {nombre_conductor[c]} esta semana, fue de: ${semana_conductor[c]} pesos\n Porcentaje equivalente: {porcentaje_recaudo[c]}%\n\n")
print(f"############################## TOTAL GENERAL: ${sum(semana_conductor)} pesos ##############################")



"""
Si el número de conductores es variable y aleatorio, sería más apropiado mantener una lista de totales acumulados para cada conductor durante la semana. Vamos a modificar el código para incorporar esta lógica:
Aquí, se ha agregado una lista llamada totales_acumulados que se inicializa con ceros para cada conductor. En el bucle principal, se acumula el recaudo para cada conductor en esta lista. Luego, al final, se utiliza esta lista para calcular el porcentaje respecto al total semanal. Esto asegura que puedas manejar un número variable de conductores sin la necesidad de crear listas adicionales.


totales_acumulados = [0] * cantidad_conductores  # Inicializamos una lista de totales acumulados para cada conductor

for dia in range(len(dias_Semana)):
    print(f"Día {dias_Semana[dia]}:")
    for conduc in range(cantidad_conductores):
        recaudo = float(input(f"Ingrese el recaudo para {nombre_conductor[conduc]} en pesos:\n$"))
        totales_acumulados[conduc] += recaudo  # Acumulamos el recaudo para cada conductor
        print("-------------------------------------------------------------")

# Calculamos el total semanal
total_semanal = sum(totales_acumulados)

# Mostramos los resultados
print(f"\nEl recaudo total de la semana es: ${total_semanal} pesos\n")

for conduc in range(cantidad_conductores):
    porcentaje = (totales_acumulados[conduc] / total_semanal) * 100
    print(f"Conductor: {nombre_conductor[conduc]} - Porcentaje respecto al total: {porcentaje:.2f}%")
"""
