# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:11:47 2026

@author: henri
"""

### fyll inn antall km kjlrt per år
km = 10000

### definisjon av kostnader
f_el = 5000 # årlig kostnad forsikring elbil
f_fossil = 7500 # årlig kostnad forsikring bensinbil
f_trafikk = 8.38 * 365 # årlig kostnad trafikkforsikring
forbruk_el = 0.2 * km * 2 # kostnad forbruk elbil
forbruk_fossil = 1 * km # kostnad forbruk bensinbil
bom_el = 0.1 * km # bomavgifter elbil
bom_fossil = 0.3 * km #bomavgifter fossilbil

total_el = f_el + f_trafikk + forbruk_el + bom_el
total_fossil = f_fossil + f_trafikk + forbruk_fossil + bom_fossil

### beregning av årskostnader for elbil og bensinbil
print("Ved", km, "kjørte km årlig, er")
print("årlig totalkostnad fpr elbil:", total_el, "kr")
print("årlig totalkostnad for bensinbil", total_fossil, "kr")

### beregning av kostnadsdifferanse
total_diff = total_el - total_fossil
print("Differanse (elbil - bensinbil):", total_diff, "kr/år")