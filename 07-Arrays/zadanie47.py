# funkcja tworzy i zwraca tablice 2D o wymiarach x wierszy na y kolumn wypelniona zerami
def create_2d_arr(x, y):
    # tworze pusta glowna liste, do ktorej bede wrzucac kolejne wiersze
    array = []
    # zewnetrzna petla wykona sie x razy (tyle ile ma byc wierszy)
    for i in range(x):
        # tworze nowy, pusty wiersz
        row = []
        # wewnetrzna petla wrzuci do tego wiersza y zer (tyle ile ma byc kolumn)
        for j in range(y):
            row.append(0)
        # gotowy wiersz zer dokladam do glownej tablicy
        array.append(row)
    # zwracam cala zbudowana tablice 2D
    return array

# wywoluje funkcje dla 3 wierszy i 5 kolumn i zapisuje wynik w zmiennej arr
arr = create_2d_arr(3, 5)

# wypisuje tablice wiersz po wierszu, zeby bylo widac uklad 3 na 5
for row in arr:
    print(row)