# lista z wynikami testu gdzie true to dobra odpowiedz a false to zla
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# licze ile bylo wszystkich pytan na tescie
question_number = len(test_results)

# zliczam poprawne odpowiedzi przechodzac petla przez cala liste
correct_answers = 0
for answer in test_results:
    # jesli odpowiedz jest prawdziwa to podbijam licznik o 1
    if answer == True:
        correct_answers += 1

# obliczam bledne odpowiedzi odejmujac poprawne od wszystkich
incorrect_answers = question_number - correct_answers

# wyliczam procent poprawnych odpowiedzi
correct_percentage = (correct_answers / question_number) * 100

# drukuje cale podsumowanie wynikow
print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers:', round(correct_percentage, 2), '%')