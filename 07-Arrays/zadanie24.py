# tworze tablice z podanymi wartosciami
numbers = [15, 8, 31, 47, 2, 19]

# ustawiam zmienna na sume elementow oraz indeks startowy na zero
total = 0
i = 0

# przechodze petla while po wszystkich elementach tablicy
while i < len(numbers):
    # dodaje kolejna liczbe spod biezacego indeksu do sumy
    total += numbers[i]
    # zwiekszam indeks o 1 zeby przejsc dalej
    i += 1

# obliczam srednia dzielac sume przez liczbe elementow
mean = total / len(numbers)

# wyswietlam tablice oraz obliczona srednia arytmetyczna
print("Array:", numbers)
print("Arithmetic mean:", round(mean, 2))