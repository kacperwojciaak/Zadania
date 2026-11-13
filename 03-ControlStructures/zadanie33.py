# pobieram imie od usera z klawiatury
name = input('Podaj imię: ')

# sprawdzam czy ostatnia litera to a
# uzywam indeksu -1 zeby dobrac sie do samego konca tekstu
# dodaje tez warunek na duze A tak na wszelki wypadek gdyby ktos wpisal calosc capslockiem
if name[-1] == 'a' or name[-1] == 'A':
    
    # jak warunek siadzie to wypluwam na ekran to co chcieli w zadaniu
    print(f'{name} -- polskie imię żeńskie')