import math

# pobieramy obwod drzewa od uzytkownika i zamieniamy na liczbe
circumference = float(input("Enter tree circumference in cm: "))

# liczymy srednice ze wzoru (obwod podzielony przez pi) i sprawdzamy czy wynosi co najmniej 50
can_be_cut = (circumference / math.pi) >= 50

# wypisujemy wynik True/False
print(f"Tree can be cut down: {can_be_cut}")