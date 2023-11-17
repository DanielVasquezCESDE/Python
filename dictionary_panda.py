import pandas as pd

deportes = { 
    "Terrestres":["Marcial arts", "Soccer", "Atletism"],
    "Aereo":["Bungee", "Parachutes", "Gymnastics"],
    "Acuáticos":["Waterpool", "Nado sincronizado", "Buceo"] #Serie
    }

#pip list - gestor de paquetes de Python

matriz = pd.DataFrame(deportes)
print(matriz)
