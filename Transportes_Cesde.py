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

dias_Semana = "Lunes", "Martes", "Miércoles", "Jueves", "viernes", "Sábado", "Domingo",

cantidad_conductores = int(input("Ingrese la cantidad de conductores de los que se registra el recaudo bruto:\n"))

nombre_conductor = []
recaudo_dia_conductor = []
recaudo_semanal_conductor = []
suma_recaudo_semanal = []

for nombre in range(cantidad_conductores):
    nombre_conductor.append(input(f"Ingrese el nombre del conductor Nro. {nombre+1}\n"))

for dia in range(7):
    print(f"Ingrese el recaudo registrado para el {dias_Semana[dia]}:\n")
    for driver in range(cantidad_conductores):
        print(f"                   Conductor(a): {nombre_conductor[driver]}         ")
        recaudo_dia_conductor.append(int(input(f"Ingrese el dinero total recaudado para el {dias_Semana[dia]} por {nombre_conductor[driver]} en pesos:\n")))
        print("-------------------------------------------------------------")
    print("################################################################################")
    suma_recaudo_semanal += int(recaudo_dia_conductor[driver])
    recaudo_semanal_conductor.append(suma_recaudo_semanal[driver])
        
    
for day in range(7):
    print(f"Día {dia}\n")
    for conduc in range(cantidad_conductores):
        print(f"----- Conductor: {nombre_conductor[conduc]}\n Recaudado del {day}: ${recaudo_dia_conductor[conduc]} pesos\n -----")
        print(f"Acumulado hasta {day}: ${recaudo_semanal_conductor[day]} pesos")
    print("\n                                                     \n")



"""recaudo_porcentaje

recaudo_total
"""
Semana = {
    "Lunes":{
        "Conductor":[],
        "Recaudo":[],
    },
    "Martes":[],
    "Miércoles":[],
    "Jueves":[],
    "Viernes":[],
    "Sábado":[],
    "Domingo":[],
}