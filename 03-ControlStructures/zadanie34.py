# pobieram od usera wiek psa i rzutuje to na inta zeby dalo sie latwo liczyc
human_years = int(input('Podaj wiek psa w latach ludzkich: '))

# robie sobie pusta zmienna na wiek zeby ja pozniej uzupelnic
dog_years = 0

# sprawdzam czy pies ma 2 lata albo mniej bo wtedy jest inny przelicznik
if human_years <= 2:
    # mnoze lata razy 10.5 tak jak podali w zadaniu
    dog_years = human_years * 10.5
    
# jak ma wiecej niz 2 lata to wlatuje tutaj
else:
    # za pierwsze 2 lata dodaje od razu sztywno 21 i dodaje reszte lat pomnozona przez 4
    dog_years = 21 + (human_years - 2) * 4

# wypluwam wynik za pomoca f-stringa i dorzucam inta zeby obciac po przecinku jak wyjdzie liczba calkowita
print(f'Wiek psa w latach psich wynosi {int(dog_years)} lata.')