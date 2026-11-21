# laduje moj modul do sprawdzania przedzialu
import range_check

# ustawiam poczatek i koniec zakresu
x = 2
y = 15

# pobieram liczbe od uzytkownika
num = int(input('A number: '))

# sprawdzam funkcja z modulu czy liczba jest w srodku i zamieniam wynik na yes albo no
if range_check.is_in_range(num, x, y):
    answer = 'yes'
else:
    answer = 'no'

# wypisuje gotowy komunikat na ekranie
print(f'Number {num} in the range <{x},{y}>: {answer}')