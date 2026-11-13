import random

# losuję trzy rzuty kostką od 1 do 6
dice_roll_1 = random.randint(1, 6)
dice_roll_2 = random.randint(1, 6)
dice_roll_3 = random.randint(1, 6)

# sumuję wszystkie wyrzucone oczka
total = dice_roll_1 + dice_roll_2 + dice_roll_3

# wyświetlam wyniki oraz sumę
print(f"Wyniki: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}")
print(f"Suma: {total}")