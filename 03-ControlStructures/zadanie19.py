# zeruje zmienna na sume liczb parzystych
sum = 0

# lecimy petla od 1 do 10 wiec dajemy zakres do 11
for i in range(1, 11):
    # jesli reszta z dzielenia przez 2 to nie zero czyli liczba jest nieparzysta to pomijamy
    if i % 2 != 0:
        continue
    # dodaje parzysta liczbe do sumy
    sum += i

# wyswietlam ostateczny wynik sumy liczb parzystych
print(f'Sum of even numbers in the range <1,10> is {sum}')