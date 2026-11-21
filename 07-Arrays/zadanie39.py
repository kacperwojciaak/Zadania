# tworze dwie tablice do sprawdzenia
arr1 = [3, 7, 1]
arr2 = [9, 1, 5, 3, 8, 7]

# zakladam na start ze pierwsza tablica jest podzbiorem drugiej
is_subset = True

# lece petla po kazdym elemencie z pierwszej tablicy
for item in arr1:
    # jesli chociaz jednej liczby brakuje w drugiej tablicy to zmieniam wynik na False
    if item not in arr2:
        is_subset = False
        # przerywam petle bo nie ma juz sensu sprawdzac reszty elementow
        break

# wyswietlam obie tablice oraz koncowy wynik
print("Array 1:", arr1)
print("Array 2:", arr2)
if is_subset:
    print("Result: Array 1 is a subset of Array 2")
else:
    print("Result: Array 1 is not a subset of Array 2")