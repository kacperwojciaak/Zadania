# pobieram prędkość od użytkownika i zamieniam na liczbę
speed = int(input("Enter vehicle speed: "))

# sprawdzam czy mieści się w naszym przedziale od 40 do 140
is_valid = 40 <= speed <= 140

# wypisuję wynik na ekran
print(f"Speed is valid: {is_valid}")