# tworze tablice z liczbami z przykladu
numbers = [8, 2, 5, 1, 9]

# wypisuje oryginalna tablice w jednej linii
print("Array:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

# przechodze petla po kazdej liczbie i wypisuje jej druga potege
print("2nd power:", end=" ")
for num in numbers:
    # podnosze liczbe do kwadratu za pomoca operatora **
    print(num ** 2, end=" ")
print()