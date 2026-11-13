# pobieram wiek od uzytkownika i odrazu zamieniam na inta zeby sprawdzic liczby
age = int(input('Enter your age: '))

# sprawdzam czy wiek jest mniejszy niz 18 lub wiekszy rowny 65 uzywajac operatora or
if age < 18 or age >= 65:
    print('Zniżka przysługuje')
else:
    # jesli ma od 18 do 64 lat wlacznie to nie ma znizki
    print('Brak zniżki')