# tworze tablice z liczbami z przykladu
arr = [7, 9, 2, 4, 5, 6]

# wypisuje oryginalna tablice przed rozdzieleniem
print("arr =", arr)

# robie dwie puste listy na liczby parzyste i nieparzyste
even = []
odd = []

# lece petla po kazdej liczbie i wrzucam ja do odpowiedniego worka
for num in arr:
    # jesli reszta z dzielenia przez 2 wynosi 0 to liczba jest parzysta
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

# sklejam obie listy (najpierw parzyste potem nieparzyste) i zapisuje w arr
arr = even + odd

# wyswietlam tablice po zmianie
print("arr =", arr)