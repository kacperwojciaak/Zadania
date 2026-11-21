# laduje moj modul do liczenia liter
import letters

# zapisuje tekst z polecenia do zmiennej
sample_text = "You never get a second chance to make a first impression"

# wywoluje funkcje z mojego modulu zeby policzyc litere e
result = letters.count_letter(sample_text, 'e')

# wypisuje tekst i wynik na ekranie
print(sample_text)
print(f"The number of letter 'e': {result}")