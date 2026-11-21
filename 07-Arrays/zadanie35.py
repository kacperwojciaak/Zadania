# tworze krotke z liczbami z przykladu
my_tuple = (50, 20, 40, 50, 30, 50)

# wpisuje wartosc ktorej wystapienia chce policzyc
value = 50

# zliczam ile razy podana liczba pojawia sie w krotce
occurrences = my_tuple.count(value)

# wyswietlam zawartosc krotki, szukana liczbe i wynik zliczania
print("Tuple:", ",".join([str(n) for n in my_tuple]))
print("Value:", value)
print("Number of occurrences:", occurrences)