# importuje wbudowany modul random do losowania
import random

# funkcja losuje indeks i zwraca element spod tego miejsca w tablicy
def rand_elem(array):
    # losuje liczbe calkowita od 0 do ostatniego indeksu tablicy
    index = random.randint(0, len(array) - 1)
    # zwracam element stojacy pod wylosowanym indeksem
    return array[index]

# tworze przykladowa tablice z liczbami
numbers = [10, 25, 33, 47, 52, 68, 74, 89]

# wyswietlam cala tablice
print("Array:", numbers)

# wywoluje funkcje 5 razy w petli zeby wypisac kilka losowych elementow
print("Random elements:", end=" ")
for i in range(5):
    print(rand_elem(numbers), end=" ")
print()