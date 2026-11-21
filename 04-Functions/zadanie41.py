# funkcja sumuje liczby od 1 do n wywolujac sama siebie
def sum_natural(n):
    # warunek stopu: suma liczb od 1 do 1 jest rowna 1
    if n == 1:
        return 1
    # dodaje aktualne n do sumy wszystkich poprzednich liczb
    if n > 1:
        return n + sum_natural(n - 1)

# obliczam i wyswietlam sume liczb naturalnych od 1 do 10
result = sum_natural(10)
print(result)