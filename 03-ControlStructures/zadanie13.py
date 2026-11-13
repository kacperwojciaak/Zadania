# pobieram dwie liczby calkowite od uzytkownika i zamieniam na inty
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

# sprawdzam czy przynajmniej jedna z liczb nie jest ujemna czyli jest wieksza lub rowna zero
if not x < 0 or not y < 0:
    print(f'At least one of the numbers {x} and {y} is not negative')
else:
    # jesli obie sa ujemne to warunek nie dziala
    print('Both numbers are negative')