# funkcja sumuje cyfry parzyste albo nieparzyste z podanej liczby
def f(number, even):
    # ustawiam sume na zero przed startem
    total = 0
    # zamieniam liczbe na tekst zeby przejsc po kazdej cyfrze po kolei
    for char in str(number):
        # zamieniam pojedynczy znak z powrotem na zwykla liczbe
        digit = int(char)
        # jesli parametr even to prawda to dodaje tylko cyfry podzielne przez dwa
        if even and digit % 2 == 0:
            total += digit
        # jesli parametr even to falsz to dodaje tylko cyfry niepodzielne przez dwa
        elif not even and digit % 2 != 0:
            total += digit
    return total

# sprawdzam funkcje na przykladach z polecenia
print(f(3124, True))
print(f(3124, False))
print(f(20576, False))
print(f(20576, True))
print(f(13115, True))