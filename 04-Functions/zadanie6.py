# definiuje funkcje ktora zamienia punkty na ocene slowna
def pts_to_grade(points):
    grade = ''
    # sprawdzam warunki od najwyzszej liczby punktow w dol
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

# przypisuje przykladowa liczbe punktow ze sprawdzianu
test_result = 15
# wywoluje funkcje i zapisuje ocene w zmiennej
final_grade = pts_to_grade(test_result)
# drukuje wynik koncowy
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')