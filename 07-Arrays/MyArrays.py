# funkcja pomocnicza sortujaca kopie tablicy rosnaco bez uzycia wbudowanych funkcji
def sort_copy(array):
    # robie kopie tablicy zeby nie popsuc kolejnosci w oryginale
    arr = array[:]
    n = len(arr)
    # sortowanie babelkowe od najmniejszej do najwiekszej
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 1. funkcja zwraca drugi co do wielkosci element tablicy
def second_largest(array):
    sorted_arr = sort_copy(array)
    # przedostatni element w posortowanej tablicy to druga najwieksza liczba
    return sorted_arr[-2]

# 2. funkcja zwraca roznice miedzy najwieksza i najmniejsza wartoscia
def min_max_diff(array):
    sorted_arr = sort_copy(array)
    return sorted_arr[-1] - sorted_arr[0]

# 3. funkcja oblicza i zwraca mediane liczb w tablicy
def median(array):
    sorted_arr = sort_copy(array)
    n = len(sorted_arr)
    mid = n // 2
    # jesli ilosc liczb jest nieparzysta to biore dokladnie srodkowy element
    if n % 2 == 1:
        return sorted_arr[mid]
    # jesli parzysta to licze srednia z dwoch srodkowych liczb
    else:
        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2

# 4. funkcja zwraca dwuelementowa tablice [najmniejsza, najwieksza]
def min_max(array):
    sorted_arr = sort_copy(array)
    return [sorted_arr[0], sorted_arr[-1]]

# 5. funkcja zwraca elementy tablicy jako tekst oddzielony myslnikami
def as_string(array):
    return "-".join([str(num) for num in array])