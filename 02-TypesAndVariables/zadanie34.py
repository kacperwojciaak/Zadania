# pobieramy liczbe od uzytkownika i zamieniamy na inta
number = int(input("Enter number: "))

# sprawdzamy reszte z dzielenia przez 2 - jesli wynosi 0, to liczba jest parzysta
even = (number % 2 == 0)

# wypisujemy wynik True/False
print(f"Number is even: {even}")