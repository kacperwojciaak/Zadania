# pobieram z klawiatury kod ean jako zwykly tekst bo tak mi bedzie najlatwiej sprawdzic jego dlugosc
ean = input('Wprowadź numer artykułu EAN-13: ')

# najpierw sprawdzam czy gosc na pewno wpisal rowne 13 znakow 
# i dla pewnosci dorzucam isdigit zeby sprawdzic czy wpisal same cyfry a nie jakies litery
if len(ean) == 13 and ean.isdigit():
    
    # jak oba warunki siadly to wypisuje ze numer jest legitny
    print('Numer artykułu jest poprawny')
    
    # teraz jak juz wiem ze kod jest git to sprawdzam czy pierwsze 3 cyfry to 590
    # uzywam do tego wycinka stringa tak zwanego slicea ktory bierze znaki od zera do trojki
    if ean[:3] == '590':
        
        # jak tak to znaczy ze to nasz polski produkt i wale komunikat
        print('Artykuł wyprodukowany w Polsce')
        
# w sumie w poleceniu nie kazali pisac bledu ale dorzucam else zeby program nie byl taki gluchy jak wpisze bzdury
else:
    print('Numer artykułu jest niepoprawny')