# funkcja sortuje tablice rosnaco metoda babelkowa
def bubble_sort(arr):
    # pobieram dlugosc tablicy zeby wiedziec ile razy przejsc petla
    n = len(arr)
    # zewnetrzna petla pilnuje liczby przejsc po calej tablicy
    for i in range(n):
        # wewnetrzna petla porownuje sasiednie elementy az do nieposortowanej czesci
        for j in range(n - i - 1):
            # jesli lewy element jest wiekszy od prawego to zamieniam je miejscami
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # zwracam posortowana juz tablice
    return arr

# tworze pierwsza liste ze spalaniem i wyswietlam ja przed oraz po sortowaniu
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(sorted_car_fuel_consumption)

# tworze druga liste z transakcjami i robie dokladnie to samo
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)