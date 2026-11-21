# importuje moj modul keyboard z tego samego folderu
import keyboard 

# pobieram wszystkie dane pracownika uzywajac funkcji z mojego modulu
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')

# wypisuje dane pracownika na ekranie
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)

# drukuje pensje tylko wtedy gdy nie kazalem jej ukryc
if not is_salary_hidden:
    print('Salary:', salary)