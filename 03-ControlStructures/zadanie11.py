# ustalam poprawne dane logowania
login = 'joe'
password = 'abcd'

# pobieram login i haslo wpisane przez uzytkownika z klawiatury
entered_login = input('Login: ')
entered_password = input('Password: ')

# sprawdzam czy login i haslo zgadzaja sie z tymi prawidtowymi uzywajac operatora and
if login == entered_login and password == entered_password:
    print('You are logged in')
else:
    # jesli chociaz jedna rzecz jest zla to wyrzuca blad
    print('Incorrect login or password!!')