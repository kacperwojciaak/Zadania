# Program wyliczający wypłatę z uwzględnieniem ewentualnej premii

basic_salary = 5000 # stała podstawa wypłaty
total_salary = 0 # zmienna przygotowana na wynik końcowy
bonus = 0.30 # premia to 30%, więc dziesiętnie zapisujemy jako 0.30

# pobieram z klawiatury odpowiedź (Y/N) na pytanie, czy gość dostaje premię.
# dopisek "== 'Y'" sprawia, że jeśli wpiszę Y, do zmiennej wpadnie True. 
# Jeśli wpiszę cokolwiek innego (np. N), wpadnie False.
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    # jeśli is_bonus to True, liczymy wypłatę z uwzględnieniem premii
    # podstawa + (podstawa * 0.30)
    total_salary = basic_salary + (basic_salary * bonus)
else:
    # jeśli is_bonus to False, total_salary to po prostu goła podstawa
    total_salary = basic_salary

# wyświetlam wszystko ładnie sformatowane f-stringami
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')