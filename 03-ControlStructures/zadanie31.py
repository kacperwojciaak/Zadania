# pytam usera o wiek i od razu zamieniam to na liczbe zeby moc sprawdzac przedzialy
age = int(input('Podaj swój wiek: '))

# sprawdzam czy ma mniej niz 13 lat
if age < 13:
    print('Należysz do grupy: Dziecko')
    
# jak wyzej nie siadlo to patrze czy lapie sie w przedziale od 13 do 19 lat wlacznie
elif 13 <= age <= 19:
    print('Należysz do grupy: Nastolatek')
    
# analogicznie sprawdzam czy wiek to przedzial miedzy 20 a 64 lata
elif 20 <= age <= 64:
    print('Należysz do grupy: Dorośli')
    
# jak zadne z powyzszych nie pyklo to logiczne ze ma 65 lat albo wiecej wiec daje sam else
else:
    print('Należysz do grupy: Senior')