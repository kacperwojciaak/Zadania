# przypisuje nazwe uniwersytetu na ktorym studiuje do zmiennej
university = 'Krakow University of Economics'

# tworze puste pudelko na nowa nazwe z dodatkowymi spacjami
university_expanded = ''

# przechodze petla po kazdym znaku w nazwie uniwersytetu
for char in university:
    # doklejam do zmiennej kazdy znak oraz dodatkowa spacje
    university_expanded = university_expanded + char + ' '

# wyswietlam oryginalna nazwe uniwersytetu
print(university)

# wyswietlam rozszerzona nazwe ze spacjami miedzy literami
print(university_expanded)