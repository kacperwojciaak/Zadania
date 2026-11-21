# laduje modul math zeby uzyc pierwiastka kwadratowego
import math

# definiuje funkcje ktora liczy pole trojkata ze wzoru herona
def triangle_area(a, b, c):
    # najpierw wyliczam polowe obwodu trojkata
    s = (a + b + c) / 2
    # podstawiam wszystko pod wzor herona i wyciagam pierwiastek
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# pobieram dlugosci trzech bokow od uzytkownika
side_a = float(input('Enter side a: '))
side_b = float(input('Enter side b: '))
side_c = float(input('Enter side c: '))

# wyswietlam wynik dla bokow wpisanych z klawiatury
print('The area of a triangle with sides', side_a, side_b, side_c, 'is', triangle_area(side_a, side_b, side_c))

# sprawdzam gotowe przyklady z polecenia
print('The area of a triangle with sides 3, 4, 5 is', triangle_area(3, 4, 5))
print('The area of a triangle with sides 5, 12, 13 is', triangle_area(5, 12, 13))
print('The area of a triangle with sides 7, 24, 25 is', triangle_area(7, 24, 25))