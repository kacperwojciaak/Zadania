# importuje modul math do obliczen trygonometrycznych oraz matplotlib do wykresu
import math
import matplotlib.pyplot as plt

# tworze dwie puste listy na katy w stopniach (x) oraz wartosci sinusa (y)
x = []
y = []

# generuje katy od 0 do 360 stopni wlacznie
for angle in range(0, 361):
    # zapisuje kat w stopniach na osi poziomej x
    x.append(angle)
    # zamieniam stopnie na radiany i obliczam sinus dla osi pionowej y
    y.append(math.sin(math.radians(angle)))

# rysuje wykres funkcji sinus
plt.plot(x, y)

# wyswietlam gotowy wykres w osobnym oknie
plt.show()