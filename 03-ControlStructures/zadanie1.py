# Program sprawdzający czy auto przekroczyło prędkość na autostradzie

speed_limit = 140 # stały limit prędkości
# pobieram prędkość z klawiatury i od razu rzutuję na int (liczbę), bo input zawsze daje tekst
car_speed = int(input('Enter car speed (km/h): ')) 

# sprawdzam, czy prędkość auta jest ostro większa niż nasz limit
if car_speed > speed_limit:
    # używam f-stringa, żeby łatwo wstrzyknąć zmienną car_speed prosto w tekst
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')