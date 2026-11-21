# funkcja zwraca n gwiazdek oddzielonych ukosnikiem
def f(n):
    # jesli n jest mniejsze lub rowne zero to zwracam pusty tekst
    if n <= 0:
        return ""
    
    # ustawiam pierwsza gwiazdke na start zeby na poczatku nie bylo ukosnika
    result = "*"
    
    # doklejam reszte gwiazdek razem z ukosnikiem o jeden raz mniej niz wynosi n
    for i in range(n - 1):
        result += "/*"
        
    return result

# sprawdzam funkcje na przykladach z polecenia
print(f(4))
print(f(1))
print(f(-1))