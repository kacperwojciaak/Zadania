# ustawiam z palca zmienne na prawda albo falsz tak jak chcieli w przykladzie
facebook = True
twitter = False
instagram = True

# musze zrobic zeby ladnie to wygladalo w konsoli i wypluwalo true false tak jak w poleceniu
print(f'facebook = {facebook}')
print(f'twitter = {twitter}')
print(f'instagram = {instagram}')

# w pythonie zmienne logiczne dzialaja tak ze True to 1 a False to 0
# wiec zeby sprawdzic ile ma kont wystarczy ze je po prostu dodam do siebie w jednej linii
liczba_kont = facebook + twitter + instagram

# no i na koniec sprawdzam czy ta suma daje mi co najmniej 2
if liczba_kont >= 2:
    
    # jak ma dwa konta albo wszystkie trzy to wale komunikat z gratulacjami
    print('Jesteś dobrym influencerem!')