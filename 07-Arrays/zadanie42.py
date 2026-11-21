# importuje modul pyplot z pakietu matplotlib pod krotka nazwa plt
import matplotlib.pyplot as plt

# podaje wspolrzedne x punktu poczatkowego (1) i koncowego (8)
xpoints = [1, 8]

# podaje wspolrzedne y punktu poczatkowego (3) i koncowego (10)
ypoints = [3, 10]

# rysuje odcinek laczacy oba punkty na wykresie
plt.plot(xpoints, ypoints)

# wyswietla gotowy wykres w osobnym oknie
plt.show()