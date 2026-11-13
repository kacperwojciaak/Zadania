# ustalam górną granicę zakresu
N = 10

# zeruje zmienna na sume liczb parzystych
sum_even = 0

# ustawiam zmienna i od której zaczynamy liczenie
i = 1

# odpalam petle while dopoki i miesci sie w zakresie do N wlacznie
while i <= N:
    # sprawdzam czy liczba jest parzysta za pomoca reszty z dzielenia
    if i % 2 == 0:
        # dodaje parzysta liczbe do sumy
        sum_even += i
    
    # zwiekszam licznik o jeden zeby petla nie dzialala w nieskonczonosc
    i += 1

# wyswietlam ostateczny wynik sumy liczb parzystych
print(f'The sum of even numbers from 1 to {N} is: {sum_even}')