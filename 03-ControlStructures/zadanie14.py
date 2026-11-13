# pobieram numer miesiaca od uzytkownika i zamieniam na inta
month = int(input('Enter month number (1..12): '))

# sprawdzam miesiace ktore maja 31 dni
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31
# sprawdzam miesiace ktore maja 30 dni
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    # luty ma zawsze 28 dni wedlug polecenia
    days = 28
else:
    days = 0
    print('Zly numer miesiaca')

# wyswietlam ile dni ma dany miesiac
print(f'Month {month} has {days} days')