# Program obliczający liczbę znaków w imieniu, nazwisku oraz pełnym imieniu i nazwisku

# Definiujemy zmienne z imieniem i nazwiskiem 
name = 'Kacper'
surname = 'Wójciak'

# Funkcja len() sprawdza długość ciągu znaków (liczbę liter)
characters_in_name = len(name)
characters_in_surname = len(surname)

# Łączymy imię i nazwisko ze spacją w środku, żeby sprawdzić długość całości
full_name = name + ' ' + surname
characters_in_full_name = len(full_name)

# Wypisujemy wyniki na ekranie
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {characters_in_surname} characters')
print(f'Your full name has {characters_in_full_name} characters')