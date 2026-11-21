# funkcja sumuje liczby z przedzialu od x do y podzielne przez 2 i 3 ale nie przez 4
def f(x, y):
    # ustawiam sume na zero przed startem
    total = 0
    # lece petla po wszystkich liczbach od x do y wlacznie
    for num in range(x, y + 1):
        # sprawdzam wszystkie trzy warunki naraz
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            # jesli liczba pasuje to dokladam ja do sumy
            total += num
    return total

# sprawdzam funkcje na przykladach z polecenia
print(f(1, 20))
print(f(10, 30))