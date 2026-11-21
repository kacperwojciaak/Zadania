# funkcja zwraca ciag skladajacy sie z n gwiazdek
def star(n):
    return "*" * n

# tworze tablice z podanymi liczbami calkowitymi
numbers = [2, 6, 4, 9, 7]

# lece petla po kazdej liczbie i wypisuje ja razem z odpowiednia liczba gwiazdek
for num in numbers:
    print(f"{num}: {star(num)}")