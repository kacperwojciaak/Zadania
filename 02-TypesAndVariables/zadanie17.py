# Program wczytujący imię i nazwisko z klawiatury

# Funkcja input() zatrzymuje program i czeka, aż użytkownik wpisze imię na klawiaturze
first_name = input('Enter your first name: ')

# Wczytujemy nazwisko w taki sam sposób do osobnej zmiennej
last_name = input('Enter your last name: ')

# Łączymy zmienne za pomocą plusów i spacji w środku w jedną całość
full_name = first_name + ' ' + last_name

# Wypisujemy osobno imię i nazwisko za pomocą f-stringa
print(f'Your first name is {first_name} and your last name is {last_name}')

# Wypisujemy połączone pełne imię i nazwisko
print(f'And your full name is {full_name}')