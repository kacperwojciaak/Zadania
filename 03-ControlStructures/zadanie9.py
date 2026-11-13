# pobieram numer miesiaca od uzytkownika i zamieniam na inta zeby dalo sie porownywac liczby
month = int(input('Enter month number (1..12): '))

# sprawdzam w jakim przedziale miesiac sie miesci zeby ustalic kwartal
if month >= 10:
    quarter = 4
elif month >= 7:
    quarter = 3
elif month >= 4:
    quarter = 2
elif month >= 1:
    quarter = 1
else:
    quarter = 'nieznany'

# wyswietlam wynik zeby widziec jaki miesiac wpadl do ktorego kwartalu
print(f'Month {month} is in quarter {quarter}')