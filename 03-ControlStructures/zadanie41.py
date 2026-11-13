# pobieram z klawiatury czas w formacie gg:mm jako zwykly tekst
time_24 = input('Wprowadź godzinę (format 24-godzinny): ')

# rozbijam ten tekst na dwie czesci uzywajac dwukropka jako separatora
# split dzieli mi to na liste wiec od razu przypisuje to do dwoch osobnych zmiennych
hours_str, minutes_str = time_24.split(':')

# rzutuje same godziny na inta zeby dalo sie robic na nich logike i matematyke
hours = int(hours_str)

# robie sobie zmienna na pore dnia i ustawiam domyslnie na rano czyli am
period = 'am'

# sprawdzam czy godzina to 12 albo wiecej
if hours >= 12:
    # jak tak to znaczy ze juz jest po poludniu wiec podmieniam na pm
    period = 'pm'
    
    # jak jest 13 albo wiecej to musze odjac 12 zeby z 16 zrobila sie 4 tak jak na zwyklym zegarku
    if hours > 12:
        hours -= 12

# musze jeszcze obsluzyc sytuacje jak ktos wpisze 00 w godzinach (czyli polnoc)
# na amerykanskim zegarku polnoc to 12 am wiec po prostu ustawiam godziny na 12
if hours == 0:
    hours = 12

# skladam to wszystko do kupy w f-stringu i wypluwam na ekran
# minuty zostawiam jako ten poczatkowy tekst zeby mi nie wcielo zera z przodu (np w 16:05)
print(f'Godzina w formacie 12-godzinnym: {hours}:{minutes_str}{period}')