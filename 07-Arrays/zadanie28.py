# tworze dwie tablice z liczbami calkowitymi z polecenia
arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

# wypisuje opis wyniku w jednej linii
print("Numbers from the first array not in the second:", end=" ")

# lece petla po kazdej liczbie z pierwszej tablicy
for num in arr1:
    # sprawdzam czy danej liczby nie ma w drugiej tablicy
    if num not in arr2:
        # jesli jej nie ma to drukuje ja na ekranie
        print(num, end=" ")
print()