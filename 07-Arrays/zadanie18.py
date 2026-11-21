import random

# gotowe wzory tablic z polecenia
arr1 = [3, 7, 1, 0, 4]
arr2 = [[2, 3], [7, 1], [0, 4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1, 10)]
arr5 = [i * 2 for i in range(1, 10)]
arr6 = [random.randint(1, 20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# tworze tablice z podanymi trzema wartosciami
arr10 = [4, 0, 3]

# tworze 15 elementowa tablice z samymi zerami
arr11 = [0 for i in range(15)]

# tworze tablice z liczbami od 1 do 30 wlacznie
arr12 = [i for i in range(1, 31)]

# losuje 20 razy liczbe 0 albo 1 do nowej tablicy
arr13 = [random.randint(0, 1) for i in range(20)]

# tworze tablice 2D majaca 5 wierszy i 2 kolumny wypelniona False
arr14 = [[False for i in range(2)] for j in range(5)]

# wypisuje wszystkie utworzone tablice po kolei
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)
print("arr5:", arr5)
print("arr6:", arr6)
print("arr7:", arr7)
print("arr8:", arr8)
print("arr9:", arr9)
print("arr10:", arr10)
print("arr11:", arr11)
print("arr12:", arr12)
print("arr13:", arr13)
print("arr14:", arr14)