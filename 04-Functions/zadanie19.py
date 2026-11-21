# funkcja liczy najmniejsza liczbe monet potrzebna do zaplaty
def f(amount_to_pay):
    # ustawiam licznik monet na zero
    coins = 0
    
    # najpierw biore jak najwiecej piatek bo sa najwieksze
    coins += amount_to_pay // 5
    # sprawdzam ile kwoty zostalo do zaplacenia po wydaniu piatek
    amount_to_pay = amount_to_pay % 5
    
    # z reszty kwoty biore jak najwiecej dwojek
    coins += amount_to_pay // 2
    # sprawdzam ile zostalo do zaplacenia po wydaniu dwojek
    amount_to_pay = amount_to_pay % 2
    
    # to co zostalo to juz same zlotowki wiec dorzucam je do licznika
    coins += amount_to_pay
    
    return coins

# sprawdzam funkcje na przykladach z polecenia
print(f(23))
print(f(8))
print(f(2))
print(f(0))