# funkcja konwertuje tablice dwuwymiarowa (2D) na zwykla liste jednowymiarowa (1D)
def convert_2d_to_1d(arr_2d):
    # tworze pusta liste jednowymiarowa na wszystkie liczby
    arr_1d = []
    # zewnetrzna petla bierze po kolei kazdy wiersz z tablicy 2D
    for row in arr_2d:
        # wewnetrzna petla wyjmuje pojedyncze liczby z tego wiersza
        for item in row:
            # wrzucam kazda liczbe po kolei do jednej wspolnej listy
            arr_1d.append(item)
    # zwracam gotowa splaszczona tablice 1D
    return arr_1d

# zapisuje trzy tablice dwuwymiarowe z polecenia
arr1 = [
    [2, 3],
    [1, 5]
]

arr2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

arr3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

# konwertuje i wyswietlam wynik dla kazdej z trzech tablic
for idx, arr in enumerate([arr1, arr2, arr3], start=1):
    print(f"1D array {idx}:", convert_2d_to_1d(arr))