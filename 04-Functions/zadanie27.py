# funkcja wylicza n-ta liczbe z ciagu fibonacciego
def f(n):
    # pierwsza liczba w ciagu to zawsze zero
    if n == 1:
        return 0
    # druga liczba w ciagu to zawsze jeden
    elif n == 2:
        return 1
        
    # ustawiam dwie pierwsze liczby jako punkt startowy
    a = 0
    b = 1
    
    # lece petla od trzeciego miejsca do n wlacznie
    for i in range(3, n + 1):
        # nowa liczba to suma dwoch poprzednich
        next_num = a + b
        # przesuwam obie zmienne o jedno miejsce do przodu
        a = b
        b = next_num
        
    return b

# sprawdzam funkcje na przykladach z polecenia
print(f(5))
print(f(9))