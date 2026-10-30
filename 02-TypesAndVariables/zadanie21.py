# Program obliczający cenę produktu po rabacie i wartość obniżki

# Wczytujemy cenę oraz rabat z klawiatury (cena jako float, rabat jako int lub float)
price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))

# Obliczamy wartość obniżki (rabat w procentach dzielimy przez 100 i mnożymy przez cenę)
reduction = price * (discount / 100)

# Obliczamy nową cenę po rabacie
price_with_discount = price - reduction

# Wypisujemy wyniki, formatując liczby do dwóch miejsc po przecinku za pomocą :.2f
print(f'Price with discount: {price_with_discount:.2f}')
print(f'Reduction: {reduction:.2f}')