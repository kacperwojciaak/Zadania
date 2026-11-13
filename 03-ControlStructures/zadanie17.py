# wpisuje tekst do zaszyfrowania
plain_text = 'The early bird catches the worm'

# tworze puste pudelko na zaszyfrowany tekst
encrypted_text = ''

# przechodze petla po kazdym znaku w tekscie
for char in plain_text:
    # pobieram kod liczbowy znaku za pomoca ord
    code = ord(char)
    
    # zwiekszam kod o jeden zeby przesunac litere w alfabecie w prawo
    new_code = code + 1
    
    # zamieniam z powrotem nowy kod liczbowy na znak za pomoca chr
    new_char = chr(new_code)
    
    # doklejam zaszyfrowany znak do nowego tekstu
    encrypted_text = encrypted_text + new_char

# wyswietlam oryginalny tekst
print(plain_text)

# wyswietlam zaszyfrowany tekst
print(encrypted_text)