# pobieram liczbe sekund od uzytkownika i zamieniam na inta
seconds = int(input('Enter the number of seconds: '))

# odliczam w pętli dopoki sekundy sa wieksze od zera
while seconds > 0:
    # sprawdzam czy to ostatnie pięć sekund żeby wypisać je słownie
    if seconds == 5:
        print('pięć')
    elif seconds == 4:
        print('cztery')
    elif seconds == 3:
        print('trzy')
    elif seconds == 2:
        print('dwa')
    elif seconds == 1:
        print('jeden')
    else:
        # dla wszystkich wiekszych liczb wypisuje zwykla cyfre
        print(seconds)
    
    # zmniejszam licznik sekund o jeden
    seconds -= 1