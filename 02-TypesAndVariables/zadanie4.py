# sprawdzam pierwsze wyrazenie: mnozenie ma pierszenstwo przed dodawaniem
wypisz_1 = 3 * 2 + 1
print("Wynik 1:", wypisz_1)

# sprawdzam drugie wyrazenie: najpierw mnozenie, potem dodawanie
wypisz_2 = 5 + 10 * 5
print("Wynik 2:", wypisz_2)

# sprawdzam trzecie wyrazenie: najpierw potegowanie, potem dzielenie, na koncu dodawanie
wypisz_3 = 4 + 4 / 2 ** 2
print("Wynik 3:", wypisz_3)

# sprawdzam czwarte wyrazenie: modulo wykonuje sie od lewej do prawej
wypisz_4 = 4 % 3 % 2 % 1
print("Wynik 4:", wypisz_4)

# sprawdzam piate wyrazenie: najpierw potega, potem modulo i mnozenie, na koncu dodawanie
wypisz_5 = 1 + 2 % 3 ** 4 * 5
print("Wynik 5:", wypisz_5)

# sprawdzam szoste wyrazenie: czy prawda jest rozna od falszu
wypisz_6 = True != False
print("Wynik 6:", wypisz_6)