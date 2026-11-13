# Pytam użytkownika ile liczb pierwszych chce wypisać. 
# int() zamienia tekst wpisany z klawiatury na prawdziwą liczbę całkowitą.
n = int(input("Podaj ile liczb pierwszych mam znaleźć: "))

# Ten licznik będzie pilnował, ile liczb pierwszych już udało mi się znaleźć i wypisać
znalezione = 0

# Zaczynam sprawdzanie od dwójki, bo to najmniejsza liczba pierwsza 
obecna_liczba = 2

print("Liczby pierwsze:", end=" ")

# Główna pętla, która kręci się tak długo, aż znajdę dokładnie 'n' liczb pierwszych
while znalezione < n:
    
    # Zakładam w ciemno, że liczba, którą teraz sprawdzam, jest pierwsza (flaga)
    jest_pierwsza = True
    
    # Sprawdzam wszystkie możliwe dzielniki od 2 do liczby o jeden mniejszej niż sprawdzana.
    for dzielnik in range(2, obecna_liczba):
        
        # Jeśli moja liczba dzieli się przez sprawdzany dzielnik bez reszty (modulo % daje 0)...
        if obecna_liczba % dzielnik == 0:
            # ...to znaczy, że znalazłem intruza! Ta liczba na pewno NIE JEST pierwsza.
            jest_pierwsza = False
            # Nie ma sensu sprawdzać dalej, zrywam tę pętlę i uciekam
            break 
            
    # Jeśli po powyższym sprawdzaniu flaga nadal mówi, że jest pierwsza, to ją wypisuję
    if jest_pierwsza == True:
        print(obecna_liczba, end=" ")
        
        # Podbijam licznik znalezionych o 1
        znalezione += 1
        
    # Biorę następną liczbę z rzędu do sprawdzenia w kolejnym obrocie głównej pętli (3, 4, 5, 6...)
    obecna_liczba += 1