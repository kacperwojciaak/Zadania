# dane z tygodniowymi wydatkami w ukladzie jedzenie transport rachunki
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# zmienne do sumowania wydatkow z podzialem na kategorie
food_total = 0
transport_total = 0
utilities_total = 0

# pusta lista w ktorej zapisze sume wydatkow dla kazdego tygodnia
week_totals = []

# zmienna na calkowite wydatki z calego miesiaca
total_expenses = 0

# lece petla po kazdym tygodniu czyli po kolejnych wierszach tablicy
for week in monthly_expenses:
    # dodaje wartosci z odpowiednich kolumn do sum dla kategorii
    food_total += week[0]
    transport_total += week[1]
    utilities_total += week[2]

    # licze sume wydatkow z biezacego tygodnia i dorzucam do listy tygodni
    current_week_sum = sum(week)
    week_totals.append(current_week_sum)

    # powiekszam calkowity koszt miesiaca o sume z tego tygodnia
    total_expenses += current_week_sum

# drukuje cale podsumowanie wydatkow
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total_expenses)