# funkcja sprawdza czy czwarta cyfra kodu zgadza sie z reszta z dzielenia sumy trzech pierwszych przez 7
def f(product_code):
    # wyciagam trzy pierwsze znaki i zamieniam kazdy z nich na liczbe
    d1 = int(product_code[0])
    d2 = int(product_code[1])
    d3 = int(product_code[2])
    
    # wyciagam czwarta cyfre kontrolna i zamieniam na liczbe
    control_digit = int(product_code[3])
    
    # sumuje trzy pierwsze cyfry
    total = d1 + d2 + d3
    
    # sprawdzam czy reszta z dzielenia sumy przez 7 jest rowna cyfrze kontrolnej
    return total % 7 == control_digit

# sprawdzam funkcje na przykladach z polecenia
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))