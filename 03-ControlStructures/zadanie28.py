# pobieram nowe hasło od użytkownika
new_password = input('Enter new password: ')

# sprawdzam czy długość hasła jest mniejsza niż 12 znaków
if len(new_password) < 12:
    # jeśli jest za krótkie to wyświetlam ostrzeżenie
    print('Password too short (min. 12 chars)')
else:
    # jeśli ma 12 lub więcej znaków to hasło jest poprawne
    print('Password is valid')