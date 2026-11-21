# lista z wynikami pomiarow temperatury z marca
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# licze ile bylo wszystkich pomiarow w tym miesiacu
measurements = len(temperatures)

# sumuje wszystkie temperatury w petli i dziele przez ich liczbe zeby miec srednia
temp_total = 0
for temp in temperatures:
    temp_total += temp
avg_temp = temp_total / measurements

# znajduje najnizsza i najwyzsza temperature przy uzyciu wbudowanych funkcji
min_temp = min(temperatures)
max_temp = max(temperatures)

# zliczam dni z ujemna temperatura uzywajac petli while
negative_temp = 0
i = 0
while i < measurements:
    # sprawdzam czy temperatura pod danym indeksem jest mniejsza od zera
    if temperatures[i] < 0:
        negative_temp += 1
    # przesuwam indeks o 1 dalej
    i += 1

# wyswietlam pelny raport pogodowy dla marca
print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:', measurements)
print('Average temperature in the month:', round(avg_temp, 2))
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of days with negative temperature:', negative_temp)