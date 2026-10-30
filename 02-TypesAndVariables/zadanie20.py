# Program obliczający kwotę oraz 23% podatku VAT

# Wczytujemy kwotę z klawiatury i zamieniamy na liczbę zmiennoprzecinkową (float)
amount_str = input('Enter amount: ')
amount = float(amount_str)

# Obliczamy podatek VAT (23% z kwoty, czyli mnożymy przez 0.23)
vat = amount * 0.23

# Wypisujemy wyniki z formatowaniem do dwóch miejsc po przecinku (oznaczenie :.2f)
print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:.2f}')