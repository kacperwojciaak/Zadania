# dane pracownika w jednym ciągu
employee = "Mr. John May, born on 1998-02-16"

# wycinam imię - od znaku nr 4 do 8 (komputer zatrzymuje się tuż przed 8, czyli przed spacją)
print(f'Name: {employee[4:8]}')

# nazwisko zaczyna się na 9 pozycji (po spacji) i kończy przed przecinkiem na 12
print(f'Surname: {employee[9:12]}')

# data zaczyna się od 22 znaku i leci do samego końca, więc po dwukropku zostawiam puste
print(f'Born: {employee[22:]}')

# inicjały to po prostu pojedyncze litery: pierwsza z imienia (4) i pierwsza z nazwiska (9)
print(f'Initials: {employee[4]}{employee[9]}')