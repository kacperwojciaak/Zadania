# przypisuje predkosc w kilometrach na godzine
speed_kmh = 70

# przeliczam km/h na m/s (dzielimy przez 3.6, bo tyle metrów na sekundę mieści się w jednym km/h)
speed_ms = speed_kmh / 3.6

# wypisuje wynik na ekranie
print(speed_kmh, "km/h = ", speed_ms, "m/s")