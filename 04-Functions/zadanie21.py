# funkcja liczy ile jest ujemnych liczb parzystych w przedziale od x do y
def f(x, y):
    # ustawiam licznik znalezionych liczb na zero
    count = 0
    # lece petla po wszystkich liczbach od x do y wlacznie
    for num in range(x, y + 1):
        # sprawdzam czy liczba jest mniejsza od zera i dzieli sie przez dwa
        if num < 0 and num % 2 == 0:
            count += 1
    return count

# sprawdzam funkcje na przykladach z polecenia
print(f(-7, 8))
print(f(-1, 11))