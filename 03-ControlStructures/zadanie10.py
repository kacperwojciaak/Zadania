# pobieram liczbe od uzytkownika i odrazu zamieniam na inta zeby sprawdzic czy wieksza czy mniejsza od zera
number = int(input('Podaj liczbę: '))

# sprawdzam czy liczba jest wieksza od zera czyli dodatnia
if number > 0:
    print(f'Liczba {number} jest dodatnia')
# sprawdzam czy jest mniejsza od zera czyli ujemna
elif number < 0:
    print(f'Liczba {number} jest ujemna')
else:
    # jesli nie jest ani plus ani minus to znaczy ze to zero
    print('Liczba wynosi 0')