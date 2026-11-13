# pobieram wzrost w centymetrach od uzytkownika
height = input('Enter your height in cm: ')

# pobieram wage w kilogramach
weight = input('Enter your weight in kg: ')

# zamieniam wzrost na liczbe calkowita
height = int(height)

# zamieniam wage na liczbe calkowita
weight = int(weight)

# liczę BMI: waga dzielona przez wzrost w metrach podniesiony do kwadratu
bmi = weight / (height/100)**2

# zaokrąglam wynik do dwóch miejsc po przecinku
bmi = round(bmi, 2)

# wypisuje wynik na ekranie
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')