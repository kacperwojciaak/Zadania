###
# Kalkulator BMI (Body Mass Index)
# Program pobiera od użytkownika wzrost i wagę, a następnie liczy wskaźnik BMI.
#

# input() zatrzymuje program i prosi użytkownika o wpisanie danych z klawiatury
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')

# Zamieniamy wpisany tekst na liczby całkowite (int - integer), żeby móc wykonywać na nich obliczenia
height = int(height)
weight = int(weight)

# Wzór na BMI: waga / (wzrost w metrach do kwadratu). 
# Dzielimy wzrost przez 100, żeby zamienić centymetry na metry. ** 2 oznacza potęgowanie.
bmi = weight / (height/100)**2

# round() zaokrągla nasz wynik do 2 miejsc po przecinku
bmi = round(bmi, 2)

# Wypisujemy gotowy wynik na ekran
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')