# importuje modul do rysowania wykresow
import matplotlib.pyplot as plt

# tworze dwie puste listy na wspolrzedne x oraz y
x = []
y = []

# generuje liczby calkowite od -10 do 10 i wrzucam je do listy x
for n in range(-10, 11):
    x.append(n)

# dla kazdego x obliczam wartosc funkcji f(x) = x^2 - 3 i zapisuje w liscie y
for n in x:
    y.append(n**2 - 3)

# rysuje wykres laczac wszystkie wyliczone punkty (x, y)
plt.plot(x, y)

# wyswietlam gotowy wykres paraboli w osobnym oknie
plt.show()