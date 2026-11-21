# funkcja oblicza wynik dodawania i odejmowania z podanego napisu
def f(expression):
    # biore pierwsza cyfre jako punkt startowy i zamieniam ja na liczbe
    total = int(expression[0])
    
    # przeskakuje co dwa znaki zaczynajac od pierwszego operatora
    for i in range(1, len(expression), 2):
        # pobieram znak dzialania plus lub minus
        operator = expression[i]
        # pobieram kolejna cyfre zaraz za operatorem i zamieniam na liczbe
        number = int(expression[i + 1])
        
        # wykonuje odpowiednie dzialanie na wyniku
        if operator == "+":
            total += number
        elif operator == "-":
            total -= number
            
    return total

# sprawdzam funkcje na przykladach z polecenia
print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))