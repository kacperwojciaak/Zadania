# pobieram liczbe od uzytkownika 
liczba = int(input("Wprowadź liczbę: "))

# krece petla od 1 do 10 uzywajac range
# wpisuje 11 bo range bierze liczby do tej podanej ale bez niej samej
for i in range(1, 11):
    
    # licze wynik mnozenia podanej liczby przez obecny krok w petli
    wynik = liczba * i
    
    # wypisuje gotowe dzialanie ladnie posklejane na ekranie
    print(f"{liczba} x {i} = {wynik}")