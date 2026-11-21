# funkcja sprawdza czy podany ciag znakow to poprawna liczba binarna
def f(binary_number):
    # lece petla po kazdym znaku w podanym tekscie
    for char in binary_number:
        # jak trafie na znak ktory nie jest zerem ani jedynka to od razu zwracam false
        if char != '0' and char != '1':
            return False
    # jak cala petla przeszla i nie bylo innego znaku to zwracam true
    return True

# sprawdzam funkcje na przykladach z polecenia
print(f("101101"))
print(f("1311a10100"))