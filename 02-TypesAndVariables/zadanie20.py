# pobieram kwotę z klawiatury i zamieniam na float, bo mogą być grosze po kropce
amount = float(input("Enter amount: "))

# liczę 23% podatku z podanej kwoty (23% to w ułamku 0.23)
vat = amount * 0.23

# wypisuję wyniki. dopisek :.2f w klamerkach zaokrągla liczbę do 2 miejsc po przecinku
print(f"Amount  : {amount:.2f}")
print(f"VAT 23% : {vat:.2f}")