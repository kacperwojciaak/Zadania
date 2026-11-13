# pobieram z klawiatury ile sztuk kupiono 
quantity = int(input('Ilość zakupionych produktów: '))

# pobieram cene za sztuke i daje we floacie jakby ktos wpisal cene z groszami
price = float(input('Cena produktu: '))

# robie sobie zmienna na sume zeby potem tylko ja nadpisac
total_to_pay = 0

# sprawdzam czy kupil dwa albo mniej bo wtedy omija go caly ten rabat
if quantity <= 2:
    # placi pelna cene wiec zwykle mnozenie ilosci przez cene
    total_to_pay = quantity * price
    
# jak kupil wiecej niz dwa produkty to zaczyna sie promka
else:
    # za pierwsze dwa placi normalnie wiec sztywno 2 razy cena
    # a za kazdy kolejny czyli ilosc minus 2 dostaje znizke wiec mnoze cene razy 0.75 zeby odciac te 25 procent
    total_to_pay = (2 * price) + ((quantity - 2) * (price * 0.75))

#  wynik z formatowaniem kropka 2f zeby dopisalo ladnie zera na koncu jak w prawdziwym sklepie
print(f'Kwota do zapłaty: {total_to_pay:.2f}')