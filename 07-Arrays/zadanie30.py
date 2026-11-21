# tworze tablice z liczbami z przykladu
numbers = [2, 3, 2, 5, 8, 1, 9, 8]

# wypisuje cala tablice w jednej linii
print("Array:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

# wypisuje tylko te liczby ktore wystepuja w tablicy dokladnie jeden raz
print("Unique elements:", end=" ")
for num in numbers:
    # sprawdzam ile razy aktualna liczba pojawia sie w calej tablicy
    if numbers.count(num) == 1:
        print(num, end=" ")
print()