# wypłata ojca
father_income = 5450

# wypłata matki
mother_income = 4920

# liczba osób w rodzinie
family_members = 5

# liczę całkowity budżet rodziny (dodaję wypłaty)
total_income = father_income + mother_income

# liczę dochód na głowę (cały budżet dzielę przez liczbę osób)
income_per_person = total_income / family_members

# wypluwam wynik z wklejonymi wyliczeniami, używam f-stringa (f przed cytatem), 
# żeby prosto wrzucić zmienne w klamerki
print(f'Total family income is {total_income}, and income per person is {income_per_person}')