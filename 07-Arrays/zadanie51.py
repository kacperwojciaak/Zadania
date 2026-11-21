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

# ide po kazdym wierszu i zamieniam w nim pierwszy element (indeks 0) z ostatnim (indeks -1)
for row in array:
    row[0], row[-1] = row[-1], row[0]

# wyswietlam tablice po zmianie
print("\nAfter:")
print_array(array)