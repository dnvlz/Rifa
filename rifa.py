nombres_boletos = """Nombre Apellido 3 boletos
Elton John 2 boletos
Larro Salía 2 boletos
Zamna Aída 4 boletos
Elba Dbunny 5 boletos
Otro Ejemplo 3 boletos"""

n = int(input("Número de ganadores: "))

import re
import random

lista_nombres = nombres_boletos.split("\n")
accentedCharacters = "áéíóúýÁÉÍÓÚñ";

lista = []
for element in lista_nombres:
    match = re.match(r"([A-Za-z"+accentedCharacters+"]+\s[A-Za-z"+accentedCharacters+"]+)\s([0-9]+)", element, re.I)
    items = match.groups()
    lista.append(items)

repeticiones = []
for element in lista:
    for times in range(int(element[1])):
        repeticiones.append(element[0])

# Una misma persona puede ganar dos premios
# ganadores = random.sample(repeticiones,n)
# print("Primer lugar:",ganadores[0])
# for num in range(1,n):
#     print(num+1,"° lugar:",ganadores[num])

# Diferentes premios implica diferentes personas
ganadores = []
while len(ganadores)<n:
    ganador = random.sample(repeticiones,1)
    if not ganador in ganadores:
        ganadores.append(ganador)

print("Primer lugar:",ganadores[0][0])
for num in range(1,n):
    print(num+1,"° lugar:",ganadores[num][0])