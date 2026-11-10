# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 19:55:53 2026

@author: henri
"""

# Arbeidskrav 2 PY1010

# %%
# Oppgave 1 
# Her ber programmet brukeren oppgi fødselsår og nåværende år. Deretter beregnes alderen.

alder = int(input("Hvilket ar er du fodt? "))
aarstall = int(input("Hvilket ar er det na? "))
alder_beregnet = aarstall - alder # Her beregnes alder basert på inputverdier
print(f"I {aarstall} fyller du {alder_beregnet} ar")

# %%
# Oppgave 2
# Her beregner programmet hvor mange pizzaer som 
# må kjøpes dersom hver elev skal ha 1/4 pizza 
import math

antall_elever = int(input("Skriv inn antall elever: "))
pizza_per_elev = 1/4
antall_pizza = pizza_per_elev * antall_elever
antall_pizza = math.ceil(antall_pizza) # Antall runder opp til nærmeste heltall fordi man må kjøpe hele pizzaer
print(f"Ved {antall_elever} elever, ma det kjopes inn {antall_pizza} pizzaer")

# %%
# Oppgave 3
# Dette programmet inneholder en funksjonen konverterer 
# vinkel fra grader til radianer basert på input gradtall, 
# og  printer radiantallet

import numpy as np

def grader_til_radianer(v_grad):
    return v_grad * np.pi / 180

# Bruker bes om å skrive inn gradtall
v_grad = float(input("Skriv inn gradtallet: "))

# Funksjon benyttes og resultatene lagres i en variabel
v_rad = grader_til_radianer(v_grad)

# Skriver ut resultatet med to desimaler
print(f"Radiantallet til vinkelen er {v_rad: .2f}")

# %%
# Oppgave 4a
# Her opprettes en dictionary med land, hovedstader, 
# og innbyggertall

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.2873]
}

# Oppgave 4b
# Her hetnes informasjon fra ordboken basert på hvilket land 
# man oppgir
land = str(input("Skriv inn land: "))
hovedstad = data[land][0]
innbyggere = data[land][1]

print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} millioner innbyggere i {hovedstad}.")

# Oppgave 4c
# Her er et program som legger til et nytt land i dictionary

# Bruker bes om å skrive inn informasjon
nytt_land = str(input("Skriv inn nytt land: "))
ny_hovedstad = str(input("Skriv inn hovedstaden: "))
nytt_innbyggertall = float(input("Skriv inn innbyggertall i millioner innbyggere: "))

# Informasjonen legges til i dictionary
data[nytt_land] = [ny_hovedstad, nytt_innbyggertall]

# Skriver ut den oppdaterte dictionary
print(data)

# %%
# Oppgave 5
# Dette programmet beregner areal og ytre omkrets 
# av en figur som består av en trekant og en halvsirkel

import math

def fun_areal_ytre_omkrets(a, b):
    areal_tre = (a * b) / 2 #beregner areal av trekant
    c = math.sqrt(a**2 + b**2) #beregner hypotenusen vha pytagoras
    omkrets_tre = a + b + c #beregner omkrets til trekant
    r = a/2 # beregner radius til halvsirkel
    areal_halvsirkel = (math.pi * r**2) / 2 #beregner areal av halvsirkel
    total_areal = areal_tre + areal_halvsirkel #beregner areal av figuren
    omkrets_halvsirkel = (2 * math.pi * r) / 2 # beregner omkrets av halvsirkel
    ytre_omkrets = omkrets_tre - a + omkrets_halvsirkel #beregner figurens ytre omkrets
    return (total_areal, ytre_omkrets)

# Bruker bes om å oppgi lengdene til trekanten
a = int(input("Skriv inn lengde a: "))
b = int(input("Skriv inn lengde b: "))

# Funksjonen benyttes og resultane lagres i to variabler
(total_areal, ytre_omkrets) = fun_areal_ytre_omkrets(a, b)

# Resultanee skrives ut med fire desimaler
print(f"Totalt areal =, {total_areal: .4f}")
print(f"Ytre omkrets =, {ytre_omkrets: .4f}")

# %%
# Oppgave 6
# Dette programmet 

import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(-10, 10, 200)
y = -x**2 - 5

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
