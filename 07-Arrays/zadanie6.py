# tworze liste z numerami rejestracyjnymi z roznych miast
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]

# ustawiam licznik zeby numerowac pasujace tablice od 1
counter = 1

# lece petla po kazdej rejestracji z listy
for car_number in polish_license_plates:
    # sprawdzam czy rejestracja zaczyna sie od liter KR albo KK
    if car_number.startswith('KR') or car_number.startswith('KK'):
        # wypisuje numer porzadkowy i pasujaca rejestracje
        print(counter, car_number)
        # podbijam licznik o 1 dopiero jak znajde auto z Krakowa
        counter += 1