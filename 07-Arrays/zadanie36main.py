# importuje wlasny modul z pliku MyArrays.py
import MyArrays

# tworze tablice z liczbami z polecenia
numbers = [7, 3, 8, 5, 2]

# wywoluje funkcje z modulu i drukuje wyniki
print("Numbers:", ",".join([str(n) for n in numbers]))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Difference (max - min):", MyArrays.min_max_diff(numbers))
print("Median:", MyArrays.median(numbers))

# wyciagam dwuelementowa tablice [min, max] i wyswietlam po przecinku
bounds = MyArrays.min_max(numbers)
print(f"Smallest and largest number: {bounds[0]},{bounds[1]}")

print("Numbers as a string:", MyArrays.as_string(numbers))