# tworze tablice z podanymi wartosciami
numbers = [15, 8, 31, 47, 2, 19]

# zmienna do sumowania wszystkich liczb z tablicy
total = 0

# przechodze petla for po kazdym elemencie i dokladam go do sumy
for num in numbers:
    total += num

# obliczam srednia arytmetyczna dzielac sume przez ilosc elementow
mean = total / len(numbers)

# wyswietlam cala tablice oraz wynik sredniej
print("Array:", numbers)
print("Arithmetic mean:", round(mean, 2))