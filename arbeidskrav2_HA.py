# Arbeidskrav 2 PY1010

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# %%
# Oppgave 1 
alder = int(input("Hvilket ar er du fodt?"))
aarstall = int(input("Hvilket ar er det na?"))
alder_beregnet = aarstall - alder
print(f"I {aarstall} fyller du {alder_beregnet} ar")

# %%
# Oppgave 2
antall_elever = int(input("Skriv inn antall elever:"))
pizza_per_elev = 1/4
antall_pizza = pizza_per_elev * antall_elever
# runde opp til helt tall
antall_pizza = math.ceil(antall_pizza)
print(f"Ved {antall_elever} elever, ma det kjopes inn {antall_pizza} pizzaer")

# %%
# Oppgave 3
def grader_til_radianer(v_grad):
  return v_grad * np.pi / 180

v_grad = float(input("Skriv inn gradtallet:"))
v_rad = grader_til_radianer(v_grad)

print(f"Radiantallet til vinkelen er {v_rad: .2f}")

# %%
# Oppgave 4a
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.2873]
}

# Oppgave 4b
land = str(input("Skriv inn land: "))
hovedstad = data[land][0]
innbyggere = data[land][1]

print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} millioner innbyggere i {hovedstad}.")

# Oppgave 4c
nytt_land = str(input("Skriv inn nytt land: "))
ny_hovedstad = str(input("Skriv inn hovedstaden: "))
nytt_innbyggertall = float(input("Skriv inn innbyggertall i millioner innbyggere: "))

data[nytt_land] = [ny_hovedstad, nytt_innbyggertall]

print(data)

# %%
# Oppgave 5
def fun_areal_ytre_omkrets(a, b):
    areal_tre = (a * b) / 2
    c = math.sqrt(a**2 + b**2)
    omkrets_tre = a + b + c
    r = a/2
    areal_halvsirkel = (math.pi * r**2) / 2
    total_areal = areal_tre + areal_halvsirkel
    omkrets_halvsirkel = (2 * math.pi * r) / 2
    ytre_omkrets = omkrets_tre - a + omkrets_halvsirkel
    return (total_areal, ytre_omkrets)

a = int(input("Skriv inn lengde a: "))
b = int(input("Skriv inn lengde b: "))

(total_areal, ytre_omkrets) = fun_areal_ytre_omkrets(a, b)

print(f"Totalt areal =, {total_areal: .4f}"))
print(f"Ytre omkrets =, {ytre_omkrets: .4f}")

