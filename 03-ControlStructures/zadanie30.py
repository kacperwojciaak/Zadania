# pobieram od usera ile godzin auto stalo na parkingu i od razu rzutuje to na inta zeby moc robic na tym dzialania
hours = int(input('Podaj liczbę godzin parkowania: '))

# sprawdzam czy czas parkowania to miedzy 1 a 2 godziny wlacznie
if 1 <= hours <= 2:
    fee = 5
    print(f'Opłata za parking wynosi: {fee} zł')
    
# jak wyzej nie siadlo to sprawdzam czy stal od 3 do 6 godzin
elif 3 <= hours <= 6:
    fee = 15
    print(f'Opłata za parking wynosi: {fee} zł')
    
# jak stal dluzej niz 6 godzin to placi maxa
elif hours > 6:
    fee = 20
    print(f'Opłata za parking wynosi: {fee} zł')
    
# zabezpieczam sie jakby ktos wpisal ze stal 0 albo jakas wartosc na minusie
else:
    print('Podano błędną liczbę godzin')