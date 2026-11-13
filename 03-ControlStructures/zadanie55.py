# Zanim zacznę, muszę sprowadzić z systemu Pythona specjalną skrzynkę z narzędziami
# do losowania, która nazywa się 'random'.
import random

# Odpalam pętlę, która zakręci się dokładnie 20 razy, żeby wypluć 20 liczb.
for i in range(20):
    
    # Wyciągam z mojej skrzynki 'random' narzędzie 'randint' (losuj liczbę całkowitą).
    # Podaję mu w nawiasie przedział od 5 do 10. Wynik zapisuję do pojemnika 'losowa'.
    losowa = random.randint(5, 10)
    
    # Wypisuję wylosowaną liczbę na ekranie. 
    # Dopisek end=" " ustawia je w jednym rzędzie obok siebie, zamiast w słupku.
    print(losowa, end=" ")