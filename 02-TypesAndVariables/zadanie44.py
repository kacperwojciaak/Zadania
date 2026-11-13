# przypisuję wzrost w cm
cm = 170

# liczę stopy za pomocą dzielenia bez reszty (przyjmując, że stopa to ok. 30.48 cm)
feet = int(cm // 30.48)

# liczę resztę z centymetrów i zamieniam na cale (cal to ok. 2.54 cm)
inches = int((cm % 30.48) / 2.54)

# wypisuję gotowy wynik na ekran
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')