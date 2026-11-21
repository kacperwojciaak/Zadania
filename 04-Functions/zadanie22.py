# funkcja sprawdza czy chociaz jedna z trzech liczb jest na minusie
def f(n1, n2, n3):
    # jesli pierwsza lub druga lub trzecia liczba jest mniejsza od zera to zwracam true
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    else:
        return False

# sprawdzam funkcje na przykladach z polecenia
print(f(11, 6, -4))
print(f(5, 4, 14))