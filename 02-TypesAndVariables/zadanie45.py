# pobieram kod SWIFT z klawiatury
swift = input("Podaj kod SWIFT: ")

# wyciągam pierwsze 4 znaki jako kod banku
bank_code = swift[:4]

# wyciągam kolejne 2 znaki (od 4 do 6) jako kod kraju
country_code = swift[4:6]

# wypisuję wyniki na ekran
print(f"Bank Code: {bank_code}")
print(f"Country Code: {country_code}")