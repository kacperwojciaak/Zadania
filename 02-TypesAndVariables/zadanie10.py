# importuje modul math, zeby miec dostep do funkcji pierwiastka (sqrt)
import math

# podaje boki prostokata
a = 5
b = 8

# licze przekatna z twierdzenia Pitagorasa: pierwiastek z (a do kwadratu plus b do kwadratu)
diagonal = math.sqrt(a**2 + b**2)

# wypisuje wynik na ekranie
print("Length of the diagonal:", diagonal)