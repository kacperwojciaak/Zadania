# funkcja zwraca transponowana macierz m (zamienia wiersze z kolumnami)
def transpose_matrix(m):
    # sprawdzam ile wierszy i ile kolumn ma oryginalna macierz
    rows = len(m)
    cols = len(m[0])
    
    # tworze pusta liste na nowa, obrocona macierz
    transposed = []
    
    # zewnetrzna petla idzie po starych kolumnach (stana sie nowymi wierszami)
    for j in range(cols):
        new_row = []
        # wewnetrzna petla zbiera liczby z gory na dol z danej kolumny
        for i in range(rows):
            new_row.append(m[i][j])
        # gotowy pasek dokladam jako nowy wiersz
        transposed.append(new_row)
        
    return transposed

# funkcja pomocnicza drukujaca macierz w wierszach i kolumnach
def print_matrix(matrix):
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()

# zapisuje trzy macierze z polecenia
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

m2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
]

m3 = [
    [5, 6, 7, 8]
]

# transponuje i wyswietlam po kolei wszystkie trzy macierze
for idx, matrix in enumerate([m1, m2, m3], start=1):
    print(f"Transposed matrix {idx}:")
    result = transpose_matrix(matrix)
    print_matrix(result)
    print()