# Symulacja płatności kartą w terminalu

account_balance = 500 # tyle siana mamy na koncie

# pobieram kwotę do zapłaty i zamieniam na liczbę całkowitą (int), 
# żeby móc ją potem matematycznie porównać z kontem
total_payment = int(input('Enter total payment amount: '))

# sprawdzam, czy kwota do zapłaty jest mniejsza LUB RÓWNA temu, co mam na koncie
if total_payment <= account_balance:
    print('Payment completed') # kasa się zgadza, transakcja przechodzi
else:
    print('No funds') # jak chcemy wydać więcej niż mamy, odrzuca (brak środków)