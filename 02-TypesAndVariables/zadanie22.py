# wrzucam swoje dane (Kacper Wójciak)
name = 'Kacper'
surname = 'Wójciak'

# funkcja len() zlicza litery w moim imieniu . 
# wynik ląduje w nowym pojemniku characters_in_name
characters_in_name = len(name)

# wypluwam info o imieniu, ładując pojemnik z wyliczoną liczbą w klamerki
print(f'Your name has {characters_in_name} characters')

# robię to samo dla nazwiska, ale żeby było szybciej - wrzucam funkcję len() 
# bezpośrednio w środek klamerki, komputer sam to policzy w locie
print(f'Your surname has {len(surname)} characters')

# sklejam imię z nazwiskiem (dodając spację w środku, żeby się nie zlały)
full_name = name + ' ' + surname

# wypisuję długość całości, wrzucając policzenie całego sklejonego tekstu w klamerkę.
# spacja liczy się dla komputera jako normalny znak
print(f'Your full name has {len(full_name)} characters')