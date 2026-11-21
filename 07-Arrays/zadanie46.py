# tworze tablice dwuwymiarowa (3 wiersze po 5 liczb w kazdym)
array = [
    [2, 4, 1, 7, 3],
    [5, 8, 2, 6, 1],
    [9, 3, 4, 2, 7]
]

# ustawiam zmienna przechowujaca sume wszystkich liczb na zero
total_sum = 0

# zewnetrzna petla bierze po kolei kazdy wiersz z tablicy
for row in array:
    # wewnetrzna petla przechodzi przez kazda liczbe w tym wierszu
    for item in row:
        # dodaje aktualna liczbe do calkowitej sumy
        total_sum += item

# wyswietlam obliczona sume wszystkich elementow
print("Sum of all elements:", total_sum)