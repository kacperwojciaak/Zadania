# krece pierwsza petla zeby zrobic gorna czesc wzoru rosnaco od 1 do 5 gwiazdek
for i in range(1, 6):
    
    # pętla wewnetrzna ktora drukuje tyle gwiazdek jaki jest aktualny numer rzedu
    for j in range(i):
        # end spacja drukuje je obok siebie
        print("*", end=" ")
        
    # pusty print zeby zlamac linie i przejsc poziom nizej
    print()

# teraz krece druga petla zeby zrobic dolna czesc wzoru malejaco od 4 gwiazdek do 1
# range(4, 0, -1) znaczy ze zaczynam od 4, lece do zera (bez zera) i co krok odejmuje 1
for i in range(4, 0, -1):
    
    # ta petla dziala tak samo ale tym razem "i" jest coraz mniejsze wiec gwiazdek jest mniej
    for j in range(i):
        print("*", end=" ")
        
    # puste wejscie w nowa linie
    print()