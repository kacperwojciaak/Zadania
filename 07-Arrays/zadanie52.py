# funkcja tworzy i zwraca macierz jednostkowa o wymiarach n na n
def identity_matrix(n):
    # tworze pusta liste na cala macierz
    matrix = []
    # zewnetrzna petla tworzy kolejne wiersze (indeks i od 0 do n-1)
    for i in range(n):
        row = []
        # wewnetrzna petla wypelnia pojedynczy wiersz (indeks j od 0 do n-1)
        for j in range(n):
            # na glownej przekatnej numer wiersza jest rowny numerowi kolumny (i == j)
            if i == j:
                row.append(1)
            else:
                row.append(0)
        # dokladam gotowy wiersz do macierzy
        matrix.append(row)
    return matrix

# funkcja pomocnicza drukujaca tablice 2D w wierszach i kolumnach
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        # przechodze do nowej linii po wypisaniu calego wiersza
        print()

# drukuje trzy macierze jednostkowe dla rozmiarow 3, 5 oraz 8
for size in [3, 5, 8]:
    print(f"Identity matrix ({size}x{size}):")
    m = identity_matrix(size)
    print_matrix(m)
    print()  # pusta linia dla odstepu miedzy macierzami