# pobieram numer miesiaca i dnia od uzytkownika i zamieniam na inty
month = int(input('Enter month number (1..12): '))
day = int(input('Enter the day number of the month: '))

# ustawiam domyslnie ze dzien jest niepoprawny
day_ok = False

# sprawdzam miesiace majace 31 dni
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day >= 1 and day <= 31:
        day_ok = True
# sprawdzam miesiace majace 30 dni
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        day_ok = True
# sprawdzam luty ktory ma 28 dni
elif month == 2:
    if day >= 1 and day <= 28:
        day_ok = True

# przygotowuje wiadomosc tekstowa do wyswietlenia
message = f'Day {day} for the month {month}'

# wyswietlam czy dzien jest poprawny czy nie
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')