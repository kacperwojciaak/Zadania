# Program wypisujący skrót nazwy uniwersytetu

university = "Krakow University of Economics"

# Pobieramy pierwsze litery poszczególnych słów za pomocą ich indeksów w tekście:
# K - indeks 0
# U - indeks 7 (pierwsza litera w "University")
# E - indeks 21 (pierwsza litera w "Economics")
abbreviation = university[0] + university[7] + university[21]

# Wypisujemy wynik na ekranie
print(f'The abbreviation of "{university}" is {abbreviation}')