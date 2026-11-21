# pobiera zwykly tekst z klawiatury
def input_string(message):
    text = input(message)
    return text

# pobiera tekst i zamienia go na liczbe calkowita
def input_integer(message):
    number = int(input(message))
    return number

# pobiera tekst i zamienia go na liczbe z ulamkiem
def input_real(message):
    number = float(input(message))
    return number

# sprawdza czy uzytkownik wpisal y i zwraca true albo false
def input_boolean(message):
    answer = input(message)
    if answer.lower() == 'y':
        return True
    else:
        return False