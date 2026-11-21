# funkcja liczy roznice miedzy najwieksza a najmniejsza z trzech liczb
def f(number1, number2, number3):
    # szukam najwiekszej liczby z podanej trojki
    biggest = max(number1, number2, number3)
    # szukam najmniejszej liczby z podanej trojki
    smallest = min(number1, number2, number3)
    # odejmuje najmniejsza od najwiekszej i zwracam wynik
    return biggest - smallest

# sprawdzam funkcje na przykladach z polecenia
print(f(7, 4, 9))
print(f(2, 12, 8))