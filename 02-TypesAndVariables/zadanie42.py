import math

# ustalam promień koła oraz wartość PI
r = 3
pi = math.pi

# obliczam pole koła (wzór: pi * r^2)
area = pi * (r ** 2)

# obliczam obwód koła (wzór: 2 * pi * r)
circumference = 2 * pi * r

# wypisuję wyniki na ekran (zaokrąglone do 2 miejsc po przecinku)
print(f"Obwód: {circumference:.2f}")
print(f"Powierzchnia: {area:.2f}")