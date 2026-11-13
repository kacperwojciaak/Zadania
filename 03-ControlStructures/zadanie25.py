# ustawiam domyslne saldo i poczatkowy pin skladajacy sie z 4 cyfr
balance = 1000
pin = '1234'

# wchodze w petle dzialania bankomatu
while True:
    # wyswietlam menu z dostepnymi opcjami dla uzytkownika
    print('\n========================')
    print('       ATM MENU         ')
    print('========================')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Check PIN')
    print('5. Change PIN')
    print('6. Exit')
    
    # pobieram wybor uzytkownika z menu
    choice = input('Choose an option (1-6): ')
    
    # opcja pierwsza: sprawdzenie salda
    if choice == '1':
        print(f'Your current balance is: €{balance}')
        
    # opcja druga: wplata pieniedzy
    elif choice == '2':
        amount = float(input('Enter amount to deposit: '))
        balance += amount
        print(f'Successfully deposited €{amount}. New balance: €{balance}')
        
    # opcja trzecia: wyplata pieniedzy
    elif choice == '3':
        amount = float(input('Enter amount to withdraw: '))
        if amount <= balance:
            balance -= amount
            print(f'Successfully withdrew €{amount}. New balance: €{balance}')
        else:
            print('Insufficient funds!')
            
    # opcja czwarta: sprawdzenie / potwierdzenie PINu
    elif choice == '4':
        entered_pin = input('Enter your current PIN: ')
        if entered_pin == pin:
            print('PIN is correct')
        else:
            print('Incorrect PIN')
            
    # opcja piata: zmiana PINu z walidacja
    elif choice == '5':
        current_pin = input('Enter current PIN: ')
        if current_pin == pin:
            new_pin = input('Enter new 4-digit PIN: ')
            # sprawdzam czy nowy pin ma dokładnie 4 znaki i czy wszystkie to cyfry
            if len(new_pin) == 4 and new_pin.isdigit():
                pin = new_pin
                print('PIN changed successfully')
            else:
                print('Error: PIN must consist of exactly 4 digits!')
        else:
            print('Incorrect current PIN!')
            
    # opcja szósta: wyjście z programu
    elif choice == '6':
        print('Thank you for using the ATM. Goodbye!')
        break
        
    # obsluga blednego wyboru z menu
    else:
        print('Invalid option, please try again.')