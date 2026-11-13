# zeruje zmienna na sume liczb
total_sum = 0

# zeruje licznik wpisanych liczb zeby miec do sredniej
count = 0

# odpalam nieskonczona petle zeby uzytkownik wpisywal liczby
while True:
    # pobieram liczbe od uzytkownika i zmieniam na inta
    number = int(input('Enter a number (0 to stop): '))
    
    # sprawdzam czy uzytkownik wpisal zero zeby zakonczyc wpisywanie
    if number == 0:
        break
    
    # dodaje wpisana liczbe do sumy
    total_sum += number
    
    # zwiekszam licznik wpisanych liczb o jeden
    count += 1

# sprawdzam czy uzytkownik cos wpisal zeby nie dzielic przez zero
if count > 0:
    # licze srednia dzielac sume przez ilosc liczb
    average = total_sum / count
    # wyswietlam sume oraz obliczona srednia
    print(f'The total sum of the numbers is: {total_sum}')
    print(f'The average is: {average}')
else:
    print('Nie wprowadzono żadnych liczb')