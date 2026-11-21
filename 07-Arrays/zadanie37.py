# tworze tablice z dowolnymi liczbami rzeczywistymi (z ulamkami)
numbers = [2.5, 7.1, 4.0, 9.8, 1.2, 6.4, 3.7]

# wyswietlam zawartosc tablicy zeby bylo widac z czym porownujemy
print("Array:", numbers)

# pobieram wartosc z klawiatury jako float bo uzytkownik moze wpisac ulamek
threshold = float(input("Enter a number: "))

# ustawiam licznik pasujacych elementow na zero
count = 0

# lece petla po kazdej liczbie z tablicy
for num in numbers:
    # jesli liczba z tablicy jest wieksza od wpisanej to podbijam licznik o 1
    if num > threshold:
        count += 1

# wyswietlam ile elementow bylo wiekszych od podanej liczby
print(f"Number of elements greater than {threshold}: {count}")