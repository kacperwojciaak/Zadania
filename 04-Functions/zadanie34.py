# funkcja sprawdza czy haslo ma minimum 6 znakow i czy znaki sie nie powtarzaja
def f(password):
    # najpierw sprawdzam czy haslo nie jest za krotkie
    if len(password) < 6:
        return False
        
    # lece petla po kazdym znaku w hasle
    for char in password:
        # jak jakis znak pojawia sie wiecej niz raz to haslo odpada
        if password.count(char) > 1:
            return False
            
    # jak dlugosc sie zgadza i nie bylo powtorek to zwracam true
    return True

# sprawdzam funkcje na przykladach z polecenia
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))