# Zaczynam od dwóch pierwszych liczb, dokładnie tak jak kazali w poleceniu
a = 0
b = 1

# Robię pętlę, która zakręci się dokładnie 20 razy, bo potrzebuję 20 liczb
for i in range(20):
    
    # Wypisuję to, co aktualnie siedzi w zmiennej 'a'. 
    # Dopisek end=" " sprawia, że liczby drukują się obok siebie oddzielone spacją, 
    # a nie uciekają jedna pod drugą do nowej linijki.
    print(a, end=" ")
    
    # Obliczam kolejną liczbę do ciągu (suma dwóch poprzednich)
    suma = a + b
    
    # Przesuwam wszystko o jedno miejsce do przodu na następny obrót pętli:
    # Moja dotychczasowa druga liczba (b) staje się teraz pierwszą (a)
    a = b
    
    # A wyliczona przed chwilą suma staje się moją drugą liczbą (b)
    b = suma