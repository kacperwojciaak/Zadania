# Program sprawdzający, czy zaliczyliśmy test (wymagane min. 50%)

total_tasks = 20 # wszystkich zadań na teście było 20

# pobieram z klawiatury ilość zrobionych zadań i rzutuję na int
tasks_ok = int(input('Enter the number of correctly completed tasks: '))

# ustawiam zmienną (tzw. flagę) domyślnie na False (że oblane)
test_passed = False

# sprawdzam, czy zrobione zadania to co najmniej połowa wszystkich
# dzielę total_tasks przez 2 i porównuję
if tasks_ok >= (total_tasks / 2):
    test_passed = True # jak warunek spełniony, zmieniam flagę na True (zdane)

# sprawdzam stan naszej flagi i daje odpowiedni komunikat
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')