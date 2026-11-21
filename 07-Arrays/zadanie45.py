# tworze tablice dwuwymiarowa (2 wiersze i 4 kolumny) z liczbami calkowitymi
array = [
    [2, 5, 8, 1],
    [9, 4, 7, 3]
]

# zewnetrzna petla bierze po kolei kazdy wiersz z tablicy
for row in array:
    # wewnetrzna petla przechodzi przez wszystkie liczby w danym wierszu
    for item in row:
        # drukuje liczbe i dodaje po niej spacje zamiast przeskakiwac do nowej linii
        print(item, end=" ")
    # po wypisaniu calego wiersza robie pusty print(), zeby przejsc do kolejnej linijki
    print()