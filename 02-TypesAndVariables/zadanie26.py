# Program formatujący 9-cyfrowy numer telefonu za pomocą wycinków (slicing)

# Wczytujemy numer telefonu jako ciąg znaków (tekst) z klawiatury
phone = input('Enter phone number: ')

# Dzielimy numer na trzy części po 3 cyfry za pomocą indeksów i łączymy je myślnikami
formatted_phone = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:9]

# Wypisujemy sformatowany numer telefonu na ekranie
print(f'Phone number: {formatted_phone}')