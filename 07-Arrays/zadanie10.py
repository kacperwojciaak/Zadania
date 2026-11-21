# lista z cenami 10 roznych towarow
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# lista z liczba dostepnych sztuk dla kazdego towaru
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# zmienna do zliczania lacznej wartosci calego magazynu
total_value = 0

# lece petla po indeksach od 0 do 9 zeby sparowac cene z iloscia
for i in range(len(product_prices)):
    # mnoze cene danego towaru przez liczbe sztuk i dodaje do sumy
    total_value += product_prices[i] * product_quantities[i]

# wyswietlam calkowita wartosc towarow zaokraglona do dwoch miejsc po przecinku
print("Total value of all products:", round(total_value, 2))