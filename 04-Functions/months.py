# funkcja zamienia numer miesiaca na jego nazwe po angielsku
def month(n):
    # tworze liste nazw miesiecy od pierwszego do dwunastego
    names = [
        'January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'
    ]
    # sprawdzam czy podany numer miesci sie od 1 do 12
    if 1 <= n <= 12:
        # odejmuje 1 bo w pythonie liczymy elementy na liscie od zera
        return names[n - 1]
    else:
        return 'Invalid month'