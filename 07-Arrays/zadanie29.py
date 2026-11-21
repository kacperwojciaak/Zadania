# funkcja sortuje tablice rosnaco algorytmem babelkowym
def bubblesort(array):
    # pobieram dlugosc tablicy zeby wiedziec ile obrotow zrobic
    n = len(array)
    # zewnetrzna petla pilnuje kolejnych przejsc po calej liscie
    for i in range(n):
        # wewnetrzna petla porownuje sasiednie liczby ze soba
        for j in range(n - i - 1):
            # jesli lewa liczba jest wieksza od prawej to zamieniam je miejscami
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    # zwracam juz posortowana tablice
    return array

# tworze trzy dowolne tablice z liczbami calkowitymi
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [5, 1, 4, 2, 8]
arr3 = [-3, 15, 0, -10, 7, 2]

# drukuje kazda tablice przed sortowaniem i po wywolaniu funkcji
print("Array 1 before:", arr1)
print("Array 1 after:", bubblesort(arr1))
print()

print("Array 2 before:", arr2)
print("Array 2 after:", bubblesort(arr2))
print()

print("Array 3 before:", arr3)
print("Array 3 after:", bubblesort(arr3))