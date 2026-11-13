# importuje modul math, zeby uzyc funkcji pierwiastka sqrt
import math

# pobieram wysokosc obserwatora od klawiatury (w metrach) i zamieniam na liczbe dziesietna (float)
h = float(input("Enter height in meters: "))

# licze odleglosc do horyzontu ze wzoru: 3.57 razy pierwiastek z wysokosci
d = 3.57 * math.sqrt(h)

# wypisuje wynik na ekranie
print("Distance to the horizon:", d, "km")