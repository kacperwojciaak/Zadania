# pobieram cenę z klawiatury (używam float, bo są to pieniądze z ułamkiem)
price = float(input("Enter price: "))

# pobieram wielkość rabatu w procentach. to mogą być pełne liczby, 
# więc wystarczy int (np. 15, 20, 50)
discount_percent = int(input("Enter discount %: "))

# liczę ile fizycznie pieniędzy urywa nam rabat.
# (np. 15 / 100 to 0.15, mnożę to przez pełną cenę i mam kwotę obniżki)
reduction = price * (discount_percent / 100)

# liczę nową cenę, odejmując kwotę obniżki od pełnej ceny z metki
discounted_price = price - reduction

# wypluwam wszystko na ekran.
# :.2f obcina mi wszystkie pieniądze ładnie do dwóch miejsc po kropce.
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {reduction:.2f}")