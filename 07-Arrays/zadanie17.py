# tworze macierz kwadratowa 3 na 3 wypelniona samymi zerami
matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# lece petla po indeksach od 0 do 2 zeby ustawic jedynki na przekatnej
for i in range(len(matrix)):
    # glowna przekatna ma zawsze taki sam indeks wiersza i kolumny
    matrix[i][i] = 1

# wypisuje zmodyfikowana macierz w wierszach i kolumnach
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()