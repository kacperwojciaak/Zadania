# tworze tablice z podanymi liczbami calkowitymi
numbers = [34, 7, 19, 4, 21, 8]

# ustawiam licznik liczb parzystych oraz indeks startowy na zero
even_count = 0
i = 0

# przechodze petla while po wszystkich elementach tablicy
while i < len(numbers):
    # sprawdzam czy reszta z dzielenia liczby przez 2 jest rowna zero
    if numbers[i] % 2 == 0:
        # jesli liczba jest parzysta to podbijam licznik o 1
        even_count += 1
    # przesuwam indeks o 1 zeby sprawdzic kolejna liczbe
    i += 1

# wyswietlam cala tablice i liczbe znalezionych wartosci parzystych
print("Array:", numbers)
print("Number of even values:", even_count)