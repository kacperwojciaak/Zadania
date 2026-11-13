# Program sprawdzający parzystość liczby

#  pobieram liczbę z klawiatury i rzutuję na całkowitą (int)
number = int(input('Enter number: '))

# używam operatora modulo (%), który zwraca resztę z dzielenia. 
# Jeśli liczba dzieli się przez 2 bez reszty (czyli reszta = 0), to jest parzysta.
if number % 2 == 0:
    # używam f-stringa do wstrzyknięcia wpisanej liczby w komunikat
    print(f'{number} is even')
else:
    # jeśli reszta z dzielenia była inna niż zero (wypadnie 1), to mamy liczbę nieparzystą
    print(f'{number} is odd')