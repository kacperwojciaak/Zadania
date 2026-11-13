# pobieram dwie liczby od uzytkownika i odrazu zamieniam na inty zeby dzialala matematyka
number1 = int(input('Podaj pierwszą liczbę: '))
number2 = int(input('Podaj drugą liczbę: '))

# pobieram znak dzialania jako zwykly tekst bo to plus minus gwiazdka albo kreska
operator = input('Podaj znak (+, -, *, /): ')

# sprawdzam jaki znak wpisal uzytkownik zeby zrobic dobre obliczenie
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
else:
    # bezpiecznik w razie wpisania czegos glupiego
    result = 'Blad'

# wyswietlam wynik w f stringu zeby ladnie wygladalo
print(f'{number1} {operator} {number2} = {result}')