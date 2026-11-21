# funkcja znajduje n-ta liczbe pierwsza z kolei
def f(n):
    # ustawiam licznik znalezionych liczb pierwszych na zero
    count = 0
    # zaczynam sprawdzanie od dwojki bo to pierwsza liczba pierwsza
    num = 2
    
    # szukam dopoki nie znajde tyle liczb pierwszych ile wynosi n
    while count < n:
        # zakladam na start ze aktualna liczba jest pierwsza
        is_prime = True
        # sprawdzam czy dzieli sie przez jakakolwiek liczbe od 2 do niej samej
        for i in range(2, num):
            # jak dzieli sie bez reszty to nie jest liczba pierwsza i przerywam
            if num % i == 0:
                is_prime = False
                break
        
        # jesli przeszla test to podbijam licznik znalezionych liczb pierwszych
        if is_prime:
            count += 1
            # jak to byla dokladnie n-ta z kolei to zwracam ja jako wynik
            if count == n:
                return num
        
        # przechodze do sprawdzenia kolejnej liczby
        num += 1

# sprawdzam funkcje na przykladach z polecenia
print(f(1))
print(f(5))