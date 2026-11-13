# pobieramy pierwsza i druga litere od uzytkownika
first = input("Enter first letter: ")
last = input("Enter last letter: ")

# zamieniamy litery na ich kody liczbowe (ord)
first_letter_code = ord(first)
last_letter_code = ord(last)

# (abs) wartość bezwzględna, żeby wynik zawsze był dodatni, liczymy roznice miedzy kodami i odejmujemy 1, zeby wyszło ile liter jest pomiedzy nimi
number_of_letters = abs(last_letter_code - first_letter_code) - 1

# wypisujemy wynik na ekranie
print(f"Between {first} and {last} is {number_of_letters} letters")