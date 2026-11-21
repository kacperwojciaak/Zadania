# funkcja sprawdza czy szukana liczba znajduje sie w tablicy
def occur(liczba, tablica):
    # przechodze petla po kazdym elemencie z tablicy
    for item in tablica:
        # jesli trafie na podana liczbe to od razu przerywam i zwracam True
        if item == liczba:
            return True
    # jesli cala petla przeleciala i nic nie znalazla to zwracam False
    return False

# tworze tablice z podanymi liczbami
numbers = [15, 38, 7, 23, 14]

# pobieram liczbe z klawiatury i zamieniam ja z tekstu na liczbe calkowita
user_number = int(input("Number: "))

# wypisuje cala tablice w jednej linii
print("Array:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

# sprawdzam funkcja czy wpisana liczba jest w tablicy i drukuje wynik
if occur(user_number, numbers):
    print(f"Result: number {user_number} appears in the array")
else:
    print(f"Result: number {user_number} does not appear in the array")