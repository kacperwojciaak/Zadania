# pobieramy numer rejestracyjny od uzytkownika
car_number = input("Enter car registration number: ")

# sprawdzamy czy pierwsze dwie litery to KR lub KK
is_krakow = (car_number[0:2] == "KR" or car_number[0:2] == "KK")

# wypisujemy wynik True/False
print(f"Car is from Krakow: {is_krakow}")