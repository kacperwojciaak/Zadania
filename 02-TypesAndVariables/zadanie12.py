# wrzucam na sztywno liczby z zadania, cała populacja to 8 mld
total = 8000000000

# na północy siedzi 7.2 mld
north = 7200000000

# reszta to południe, więc po prostu odejmuję północ od całości
south = total - north

# wypluwam suche dane na ekran tak jak chcieli w poleceniu
print("World population: ", total)
print("Northern Hemisphere: ", north)

# liczę procent dla północy (zwykły ułamek: część przez całość razy 100) 
# i od razu drukuję wynik
print("Northern Hemisphere in %: ", (north / total) * 100)

# to samo robię dla południa - najpierw liczba ludzi
print("Southern Hemisphere: ", south)

# i na sam koniec w ten sam sposób wyliczam procent dla południa
print("Southern Hemisphere in %: ", (south / total) * 100)