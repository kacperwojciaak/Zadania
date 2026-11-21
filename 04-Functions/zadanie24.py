# funkcja laczy liczby od 1 do n w jeden ciag znakow
def f(n):
    # tworze pusty tekst do ktorego bede doklejac kolejne liczby
    result = ""
    # lece petla od 1 do n wlacznie
    for i in range(1, n + 1):
        # zamieniam liczbe na tekst i doklejam ja na koniec
        result += str(i)
    return result

# sprawdzam funkcje na przykladach z polecenia
print(f(1111))
print(f(4))