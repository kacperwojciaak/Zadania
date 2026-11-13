# pobieram tryb jazdy od uzytkownika żeby wiedziec jak auto pali
driving_mode = input('Enter driving mode (A/M/E):')

# pobieram dystans i odrazu zamieniam na inta zeby mozna bylo liczyc matmie
distance = int(input('Enter distance in km'))

# sprawdzam jaki tryb wpisal i przypisuje ile pali na 100 km
if driving_mode == 'A':
    fuel_consumption = 7 # tyle pali w auto na sto kilometrow
elif driving_mode == 'M':
    fuel_consumption = 9 # tyle w manualu
elif driving_mode == 'E':
    fuel_consumption = 6 # tyle w eco
else:
    fuel_consumption = 0
    print('zly tryb jazdy')

# liczbe calkowite zuzycie mnozac kilometry przez spalanie na sto i dzielac na sto
total_consumption = (distance * fuel_consumption) / 100

# wyswietlam gotowy wynik w f stringu
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')