# funkcja tworzy skrot z pierwszych liter kazdego slowa w tekscie
def f(name):
    # rozbijam caly tekst na osobne slowa po spacjach
    words = name.split()
    # ustawiam pusty napis do ktorego bede doklejac pierwsze litery
    acronym = ""
    
    # lece petla po kazdym slowie z listy
    for word in words:
        # biore pierwsza litere slowa i doklejam ja do wyniku
        acronym += word[0]
        
    return acronym

# sprawdzam funkcje na przykladach z polecenia
print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))