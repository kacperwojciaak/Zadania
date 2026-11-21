# funkcja zamienia pojedyncza litere na slowo z alfabetu lotniczego
def icao(letter):
    # zamieniam litere na duza zeby nie bylo problemu jak ktos wpisze mala
    letter = letter.upper()
    if letter == 'A':
        return 'Alfa'
    elif letter == 'B':
        return 'Bravo'
    elif letter == 'C':
        return 'Charlie'
    elif letter == 'D':
        return 'Delta'
    elif letter == 'E':
        return 'Echo'
    elif letter == 'F':
        return 'Foxtrot'
    elif letter == 'G':
        return 'Golf'
    elif letter == 'H':
        return 'Hotel'
    elif letter == 'I':
        return 'India'
    elif letter == 'J':
        return 'Juliett'
    elif letter == 'K':
        return 'Kilo'
    elif letter == 'L':
        return 'Lima'
    elif letter == 'M':
        return 'Mike'
    elif letter == 'N':
        return 'November'
    elif letter == 'O':
        return 'Oscar'
    elif letter == 'P':
        return 'Papa'
    elif letter == 'Q':
        return 'Quebec'
    elif letter == 'R':
        return 'Romeo'
    elif letter == 'S':
        return 'Sierra'
    elif letter == 'T':
        return 'Tango'
    elif letter == 'U':
        return 'Uniform'
    elif letter == 'V':
        return 'Victor'
    elif letter == 'W':
        return 'Whiskey'
    elif letter == 'X':
        return 'X-ray'
    elif letter == 'Y':
        return 'Yankee'
    elif letter == 'Z':
        return 'Zulu'
    else:
        return '???'

# pobieram imie albo dowolne slowo od uzytkownika
name = input('Enter your name: ')
print('Spelled text:', end=' ')

# lece petla po kazdej literze w wpisanym slowie
for char in name:
    # wywoluje funkcje dla pojedynczej litery i wypisuje obok siebie ze spacja
    print(icao(char), end=' ')