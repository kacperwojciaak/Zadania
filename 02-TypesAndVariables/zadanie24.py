# nasza długa nazwa uczelni zamknięta w zmiennej
university = "Krakow University of Economics"


abbreviation = university[0] + university[7] + university[21]

# wypluwam gotowy skrót na ekran
print(abbreviation)

# alternatywa z f-stringiem (robi to samo, ale bez tworzenia zmiennej abbreviation)
print(f'Skrót uczelni to: {university[0]}{university[7]}{university[21]}')