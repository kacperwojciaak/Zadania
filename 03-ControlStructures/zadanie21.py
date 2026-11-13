# importuje modul do losowania liczb
import random

# losuje tajna liczbe od 1 do 100
number_to_guess = random.randint(1, 100)

# zeruje zmienna na strzal uzytkownika zeby petla sie w ogole odpalila
user_guess = 0

# rzucam komunikat startowy dla gracza
print('Guess the number between 1 and 100!')

# lecimy petla dopoki uzytkownik nie trafi liczby
while user_guess != number_to_guess:
    # pobieram strzal od uzytkownika i zmieniam na inta
    user_guess = int(input('Enter your guess: '))
    
    # sprawdzam czy podana liczba jest za mala
    if user_guess < number_to_guess:
        print('Too low! Try again.')
    # sprawdzam czy podana liczba jest za duza
    elif user_guess > number_to_guess:
        print('Too high! Try again.')
    else:
        # jesli nie jest ani za mala ani za duza to znaczy ze trafione
        print('Congratulations! You guessed the correct number.')