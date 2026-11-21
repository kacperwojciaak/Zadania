# funkcja sprawdza czy w pokoju byly jednoczesnie minimum trzy osoby
def f(detector):
    # ustawiam licznik osob w srodku na zero
    people = 0
    # sprawdzam po kolei kazdy ruch w drzwiach
    for sign in detector:
        # jak ktos wchodzi to dodaje jedna osobe
        if sign == "+":
            people += 1
        # jak ktos wychodzi to odejmuje jedna osobe
        elif sign == "-":
            people -= 1
        
        # po kazdym ruchu sprawdzam czy w srodku sa juz trzy osoby
        if people >= 3:
            return True
            
    # jak petla sie skonczyla i nigdy nie bylo trzech osob to zwracam false
    return False

# sprawdzam funkcje na przykladach z polecenia
print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))