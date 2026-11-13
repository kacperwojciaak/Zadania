import random

# losuję liczbę na kostce od 1 do 6
dice_rolled = random.randint(1, 6)

# sprawdzam czy wylosowana liczba to 1 lub 6
is_special = dice_rolled == 1 or dice_rolled == 6

# wypisuję wynik oraz informację logiczną
print(f"Dice rolled: {dice_rolled}")
print(f"Special number (1 or 6): {is_special}")