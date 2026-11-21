# funkcja liczy silnie z liczby n wywolujac sama siebie
def factorial(n):
    # warunek stopu: silnia z 0 i z 1 zawsze wynosi 1
    if n == 0 or n == 1:
        return 1
    # funkcja mnozy n przez wynik silni dla liczby o 1 mniejszej
    if n > 1:
        return n * factorial(n - 1)

# obliczam i wyswietlam wynik silni dla n = 5
result = factorial(5)
print(result)