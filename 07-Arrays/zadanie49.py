# tworze tablice dwuwymiarowa z liczbami z polecenia
array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

# na start zakladam ze najmniejsza i najwieksza liczba siedzi w lewym gornym rogu (0, 0)
min_val = array[0][0]
min_row = 0
min_col = 0

max_val = array[0][0]
max_row = 0
max_col = 0

# zewnetrzna petla leci po indeksach wierszy (i = 0, 1, 2, 3)
for i in range(len(array)):
    # wewnetrzna petla leci po indeksach kolumn (j = 0, 1)
    for j in range(len(array[i])):
        # jesli aktualna liczba jest mniejsza od dotychczasowego minimum to zapisuje nowy rekord
        if array[i][j] < min_val:
            min_val = array[i][j]
            min_row = i
            min_col = j
        # jesli aktualna liczba jest wieksza od dotychczasowego maksimum to zapisuje nowy rekord
        if array[i][j] > max_val:
            max_val = array[i][j]
            max_row = i
            max_col = j

# wyswietlam znalezione wartosci oraz ich dokladne wspolrzedne
print(f"Smallest value: {min_val}, row: {min_row}, column: {min_col}")
print(f"Largest value: {max_val}, row: {max_row}, column: {max_col}")