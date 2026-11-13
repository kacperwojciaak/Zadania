# pobieram imie pierwszej osoby
person1_name = input('Wprowadź imię pierwszej osoby: ')

# pobieram jej wiek i od razu robie z tego inta zeby dalo sie porownywac z liczbami
person1_age = int(input('Wprowadź wiek pierwszej osoby: '))

# robie dokladnie to samo dla drugiej osoby zeby miec komplet danych
person2_name = input('Wprowadź imię drugiej osoby: ')
person2_age = int(input('Wprowadź wiek drugiej osoby: '))

# sprawdzam czy pierwsza i druga osoba maja minimum 18 lat uzywajac operatora and
if person1_age >= 18 and person2_age >= 18:
    # uzywam f-stringa zeby fajnie wstawic imiona prosto do tekstu
    print(f'Zarówno {person1_name} jak i {person2_name} są dorośli')
else:
    # jak przynajmniej jeden z nich ma mniej niz 18 lat to ląduje tutaj w elsie
    print(f'Albo {person1_name} albo {person2_name} nie jest dorosły')