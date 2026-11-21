# funkcja znajduje oczko kostki ktore wypadlo najwiecej razy z rzedu
def f(dice):
    # ustawiam pierwsza cyfre jako aktualnie liczona i jako rekordziste na start
    max_digit = dice[0]
    max_count = 1
    
    current_digit = dice[0]
    current_count = 1
    
    # sprawdzam kolejne rzuty zaczynajac od drugiego znaku
    for digit in dice[1:]:
        # jesli wypadla ta sama cyfra co przed chwila to wydluzam serie
        if digit == current_digit:
            current_count += 1
        else:
            # jak wypadla inna cyfra to zaczynam liczyc nowa serie od 1
            current_digit = digit
            current_count = 1
            
        # sprawdzam czy obecna seria przebila dotychczasowy rekord
        if current_count > max_count:
            max_count = current_count
            max_digit = current_digit
            
    # zamieniam zwycieska cyfre z tekstu na liczbe i zwracam wynik
    return int(max_digit)

# sprawdzam funkcje na przykladach z polecenia
print(f("5233165554211"))
print(f("2133"))