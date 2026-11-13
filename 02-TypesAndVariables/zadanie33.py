# pobieramy haslo od uzytkownika z klawiatury
password = input("Enter password: ")

# sprawdzamy czy dlugosc hasla jest wieksza lub rowna 8 znakow
password_ok = len(password) >= 8

# wypisujemy wynik (True jesli ok, False jesli za krotkie)
print(f"Password length is valid: {password_ok}")