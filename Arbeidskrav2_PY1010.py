# Arbeidskrav 2 PY1010

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Oppgave 1 
alder = int(input("Hvilket ar er du fodt?"))
aarstall = int(input("Hvilket ar er det na?"))
alder_beregnet = aarstall - alder
print(f"I {aarstall} fyller du {alder_beregnet} ar")

# Oppgave 2
import math

antall_elever = int(input("Skriv inn antall elever:"))
pizza_per_elev = 1/4
antall_pizza = pizza_per_elev * antall_elever
# runde opp til helt tall
antall_pizza = math.ceil(antall_pizza)
print(f"Ved {antall_elever} elever, ma det kjopes inn {antall_pizza} pizzaer")

# Oppgave 3
import numpy as np

def grader_til_radianer(v_grad):
  return v_grad * np.pi / 180

v_grad = float(input("Skriv inn gradtallet:"))
v_rad = grader_til_radianer(v_grad)

print(f"Radiantallet til vinkelen er {v_rad: .2f}")

# Oppgave 4

