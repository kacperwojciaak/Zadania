# funkcja podnosi liczbe x do potegi n wywolujac sama siebie
def power(x, n):
    # warunek stopu: kazda liczba podniesiona do potegi 0 daje 1
    if n == 0:
        return 1
    # mnoze podstawe x przez wynik potegowania dla wykladnika o 1 mniejszego
    if n > 0:
        return x * power(x, n - 1)

# obliczam i wyswietlam wynik 5 do potegi 3
result = power(5, 3)
print(result)