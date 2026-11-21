# funkcja usuwa wszystkie spacje z podanego zdania
def f(sentence):
    # zamieniam kazda spacje na pusty tekst i zwracam wynik
    return sentence.replace(" ", "")

# sprawdzam funkcje na przykladach z polecenia
print(f("integrated development environment"))