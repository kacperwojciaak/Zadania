### # Program obliczający odległość do horyzontu dla różnych wysokości #
import math

# Przypadek 1: Stoisz na plaży (np. Twój wzrost to ok. 1.75 m)
h_plaja = 1.75
d_plaja = 3.57 * math.sqrt(h_plaja)

print(f"1. Na plaży (wysokość {h_plaja} m): odległość do horyzontu wynosi {d_plaja:.2f} km")

# Przypadek 2: Okno hotelu nad morzem na wysokości 20 metrów
h_hotel = 20
d_hotel = 3.57 * math.sqrt(h_hotel)

print(f"2. Z okna hotelu (wysokość {h_hotel} m): odległość do horyzontu wynosi {d_hotel:.2f} km")