# definiuje funkcje ktora liczy sume cyfr podanej liczby
def sum_digits(number):
    # ucinam znak minus jesli liczba jest ujemna
    number = abs(number)
    # zamieniam liczbe na tekst zeby mozna bylo przejsc po pojedynczych cyfrach
    number_str = str(number)
    # zmienna w ktorej bede zbieral sume cyfr
    total = 0
    # petla przechodzi przez kazdy znak w napisie
    for digit in number_str:
        # zamieniam pojedynczy znak z powrotem na liczbe i dodaje do sumy
        total += int(digit)
    return total

# pobieram liczbe calkowita od uzytkownika
any_number = int(input('Enter integer number: '))
# wywoluje funkcje i zapisuje wynik
result = sum_digits(any_number)
# wyswietlam wynik na ekranie
print('The sum of the digits in the number', any_number, 'is', result)