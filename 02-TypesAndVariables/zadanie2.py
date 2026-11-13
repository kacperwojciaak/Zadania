# importuje moduł random, zeby móc losować liczby
import random

# wypisuję tytuł programu na ekranie
print("Dice rolling simulator")

# uruchomiam pętle, która wykona się 5 razy (dla pięciu rzutów)
for i in range(5):
    # losuję liczbę od 1 do 6 tak jak na normalnej kostce do gry
    dice_roll = random.randint(1, 6)
    
    # wypisuję wynik rzutu i robię spację zamiast nowej linii, zeby wyniki były w jednym rzędzie
    print(dice_roll, end=" ")