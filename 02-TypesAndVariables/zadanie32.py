# pobieramy wiek od uzytkownika i zamieniamy na liczbe calkowita
age = int(input("Enter age: "))

# sprawdzamy czy wiek miesci sie w limicie (do 26 wlacznie, czyli mniejsze lub rowne 26)
no_tax = age <= 26

# wypisujemy wynik na ekranie (True albo False)
print(f"Exemption from paying taxes: {no_tax}")