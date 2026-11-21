# tworze tablice dwuwymiarowa z ukladem planszy do kolka i krzyzyk
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# zewnetrzna petla bierze po kolei kazdy caly wiersz z planszy
for row in tic_tac_toe_board:
    # wewnetrzna petla przechodzi po pojedynczych polach w danym wierszu
    for cell in row:
        # wypisuje znak z pola i stawiam spacje zamiast przechodzic do nowej linii
        print(cell, end=" ")
    # po zakonczeniu wiersza robie pusty print zeby przejsc linijke nizej
    print()