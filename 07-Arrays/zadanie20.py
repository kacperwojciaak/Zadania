# tworze tablice z podanymi liczbami naturalnymi
numbers = [15, 8, 31, 47, 2, 19]

# wypisuje oryginalna tablice w jednej linii
print("existed array:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

# wypisuje tablice od konca idac indeksami od ostatniego do zera
print("reverse array:", end=" ")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i], end=" ")
print()