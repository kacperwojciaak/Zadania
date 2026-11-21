# funkcja sprawdza czy dwie tablice maja taka sama dlugosc i identyczne elementy
def compare(tablica1, tablica2):
    # najpierw sprawdzam czy tablice maja tyle samo elementow
    if len(tablica1) != len(tablica2):
        return False

    # lece petla po indeksach i porownuje elementy na tych samych pozycjach
    for i in range(len(tablica1)):
        # jesli chociaz jedna para sie rozni to od razu przerywam i zwracam False
        if tablica1[i] != tablica2[i]:
            return False

    # jesli petla doszla do konca i wszystko sie zgadzalo to zwracam True
    return True

# wrzucam wszystkie cztery pary tablic do jednej listy zeby je latwo sprawdzic
pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2])
]

# przechodze po kazdej parze tablic po kolei
for arr1, arr2 in pairs:
    # wypisuje pierwsza tablice w jednej linii
    print("Array1:", end=" ")
    for item in arr1:
        print(item, end=" ")
    print()

    # wypisuje druga tablice w jednej linii
    print("Array2:", end=" ")
    for item in arr2:
        print(item, end=" ")
    print()

    # wywoluje funkcje compare i wypisuje wynik porownania
    if compare(arr1, arr2):
        print("Comparison: arrays are the same")
    else:
        print("Comparison: arrays are different")
    print()