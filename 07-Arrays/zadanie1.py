# tworze liste z podanymi liczbami
arr = [2, 3, 7, 5, 4]

# wyswietlam cala tablice
print(arr)

# licze i wyswietlam ile elementow jest w tablicy
print('Number of elements', len(arr))

# wyswietlam pierwsza wartosc z indeksu 0
print('First value', arr[0])

# wyswietlam druga wartosc z indeksu 1
print('Second value', arr[1])

# wyswietlam ostatnia wartosc bez uzycia ujemnego indeksu
print('Last value', arr[len(arr) - 1])

# wyswietlam przedostatnia wartosc odejmujac 2 od dlugosci tablicy
print('Penultimate value', arr[len(arr) - 2])

# dodaje pierwsza i ostatnia liczbe i wyswietlam wynik
print('Sum of first and last value', arr[0] + arr[len(arr) - 1])

# licze srednia dzielac sume wszystkich liczb przez ich ilosc
print('Average value', sum(arr) / len(arr))

# wypisuje wszystkie elementy po kolei oddzielone spacja w jednej linii
for value in arr:
    print(value, end=" ")