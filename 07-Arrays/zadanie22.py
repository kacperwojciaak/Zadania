# tworze tablice z podanymi liczbami
numbers = [-15, 8, -31, 47, -2, 19]

# zakladam na start ze pierwsza liczba jest jednoczesnie najmniejsza i najwieksza
min_val = numbers[0]
max_val = numbers[0]

# lece petla po kazdej liczbie w tablicy
for num in numbers:
    # jesli znajde liczbe mniejsza od obecnego minimum to ja zapamietuje
    if num < min_val:
        min_val = num
    # jesli znajde liczbe wieksza od obecnego maksimum to ja zapamietuje
    if num > max_val:
        max_val = num

# wyswietlam tablice oraz znaleziona najmniejsza i najwieksza wartosc
print("Array:", numbers)
print("Minimum:", min_val)
print("Maximum:", max_val)