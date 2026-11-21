# funkcja wykonuje dzialanie matematyczne w zaleznosci od podanego znaku
def f(number1, number2, operator):
    # sprawdzam jaki operator zostal podany i zwracam wynik dzialania
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2

# sprawdzam funkcje na przykladach z polecenia
print(f(2, 3, "+"))
print(f(2, 3, "%"))
print(f(2, 3, "**"))
print(f(2, 3, "*"))
print(f(2, 3, "-"))