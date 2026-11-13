# pobieram kwote od uzytkownika i robie z niej liczbe zeby na niej liczyc
kwota = int(input("Wprowadź kwotę w złotówkach: "))

# robie sobie kopie tej poczatkowej kwoty zeby wyswietlic ja potem w podsumowaniu
oryginal = kwota

# sprawdzam ile razy piątka zmiesci sie w calosci w naszej kwocie (bez reszty)
piatki = kwota // 5

# odejmuje od glownej kwoty to, co juz wydalem w piatkach (czyli np. z 18 zostaje 3, bo wydalem 3x5=15)
kwota = kwota - (piatki * 5)

# teraz sprawdzam ile razy dwojka zmiesci sie w tym, co nam zostalo (np. w 3 zmiesci sie jedna dwojka)
dwojki = kwota // 2

# znowu odejmuje od reszty kwoty to, co wydalem w dwojkach (czyli np. z 3 zostaje 1)
kwota = kwota - (dwojki * 2)

# to, co nam zostalo na samym koncu (reszta), to automatycznie ilosc jedynek, bo nic mniejszego nie ma
jedynki = kwota

# drukuje naglowek podsumowania uzywajac naszej kopii zapasowej
print(f"Kwota {oryginal} zł w monetach:")

# drukuje po kolei ile wypadlo piatek, dwojek i jedynek
print(f"5 zł monety: {piatki}")
print(f"2 zł monety: {dwojki}")
print(f"1 zł monety: {jedynki}")