### # Program obliczający całkowity dochód rodziny oraz dochód na jedną osobę #

# Przypisujemy zarobki ojca i matki oraz liczbę członków rodziny do zmiennych
father_income = 5450
mother_income = 4920
family_members = 5

# Obliczamy całkowity dochód rodziny dodając do siebie zarobki rodziców
total_income = father_income + mother_income

# Obliczamy dochód na jedną osobę dzieląc całkowity dochód przez liczbę członków rodziny
income_per_person = total_income / family_members

# Wyświetlamy sformatowany komunikat z wynikami (używając :.2f dla ładnego zaokrąglenia kwoty do 2 miejsc po przecinku)
print(
    f"Total family income is {total_income}, and income per person is {income_per_person:.2f}"
)