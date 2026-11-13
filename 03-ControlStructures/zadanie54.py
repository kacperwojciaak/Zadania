# Zewnętrzna pętla odpowiada za rzędy. Potrzebujemy ich 7. 
# Zaczynam od 1 i kończę na 8 (komputer zatrzyma się na 7).
for rzad in range(1, 8):
    
    # Wewnętrzna pętla odpowiada za kolumny w danym rzędzie.
    # Uruchomi się 7 razy (od 0 do 6) dla każdego rzędu.
    for kolumna in range(7):
        
        # Wyliczam konkretną liczbę do wydrukowania na kuponie.
        # Biorę aktualny numer rzędu i dodaję do niego wielokrotność siódemki,
        # bo każda kolejna kolumna przeskakuje dokładnie o 7 oczek.
        liczba = rzad + (kolumna * 7)
        
        # Wypisuję obliczoną liczbę.
        # żeby cyfry ułożyły się w ładną, równą tabelę.
        # end="" blokuje ucieczkę do nowej linijki.
        print(liczba, end="\t")
        
    # Ten pusty print jest bardzo ważn, kiedy wewnętrzna pętla skończy 
    # drukować całe 7 kolumn z jednego rzędu, ten print zrzuca kursor 
    # do nowej linijki, żeby kolejny rząd zaczął się pisać pod spodem.
    print()