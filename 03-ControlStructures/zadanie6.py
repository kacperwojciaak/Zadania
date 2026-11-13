# Program do sprawdzania rozmiarów ubrań

# 1. Pobieramy od użytkownika symbol rozmiar
size = input('Enter size symbol: ')

# 2. Sprawdzamy wpisaną wartość od góry do dołu
if size == 'S':
    print('S: Small size')
elif size == 'M':
    print('M: Medium size')
elif size == 'L':
    print('L: Large size')
elif size == 'XL':
    print('XL: Extra large size')
else:
    print('Incorrect symbol')