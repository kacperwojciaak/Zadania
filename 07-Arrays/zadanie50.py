# tworze pomocnicza funkcje do wypisywania tablicy w wierszach i kolumnach
def print_array(arr):
    for row in arr:
        for item in row:
            print(item, end=" ")
        print()

# tworze tablice dwuwymiarowa o wymiarach 3 wiersze na 5 kolumn
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    [9, 8, 7, 6, 5]
]

# wyswietlam tablice przed zmiana
print("Before:")
print_array(array)

# zamieniam miejscami pierwszy wiersz (indeks 0) z ostatnim (indeks -1)
array[0], array[-1] = array[-1], array[0]

# wyswietlam tablice po zmianie
print("\nAfter:")
print_array(array)