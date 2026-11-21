# tworze tablice 5x5 wypelniona zerami z polecenia
table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# zewnetrzna petla leci po indeksach wierszy (i przyjmuje wartosci 0, 1, 2, 3, 4)
for i in range(len(table)):
    # wewnetrzna petla leci po indeksach kolumn (j przyjmuje wartosci 0, 1, 2, 3, 4)
    for j in range(len(table[i])):
        # wpisuje wynik mnozenia (dodaje 1 do indeksow bo w Pythonie liczymy od zera)
        table[i][j] = (i + 1) * (j + 1)

# wypisuje gotowa tabliczke mnozenia wiersz po wierszu
for row in table:
    for item in row:
        # formatowanie :2 wyrownuje liczby do 2 znakow zeby kolumny byly rowne
        print(f"{item:2}", end=" ")
    # przechodze do nowej linii po wypisaniu calego wiersza
    print()