# ustawiam glowny licznik i na wartosc startowa czyli 6 tak jak w starym range
i = 6

# krece zewnetrzna petla dopoki i jest wieksze lub rowne zero
while i >= 0:
    
    # ustawiam drugi licznik j na 1 zeby zaczac wyliczanie od lewej strony klawiatury
    j = 1
    
    # krece wewnetrzna petla dopoki j nie dobije do 3 bo mamy 3 klawisze w jednym rzedzie
    while j <= 3:
        
        # drukuje sume obu licznikow i dodaje spacje na koncu zeby cyfry staly obok siebie
        print(f'{i+j}', end=' ')
        
        # podbijam licznik j o jeden zeby wewnetrzna petla krecila sie do przodu
        j += 1
        
    # puste print zeby zlamac linie i zejsc nizej kiedy wypisze juz caly rzad trzech cyfr
    print()
    
    # odejmuje 3 od glownego licznika zeby w nastepnym kółku wypisywac o trzy cyfry mniejsze wartosci
    i -= 3