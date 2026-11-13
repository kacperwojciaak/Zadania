# ustawiam na sztywno zmienne z cenami tak jak chcieli w poleceniu
current_price = 140.00
previous_price = 200.00

# wypluwam na ekran biezaca i stara cene i uzywam formatowania .2f zeby pokazalo ladnie grosze tak jak w przykladzie
print(f'Aktualna cena produktu: {current_price:.2f}')
print(f'Poprzednia cena produktu: {previous_price:.2f}')

# licze ile procent wyniosla znizka
# najpierw roznica w cenie potem dziele przez stara cene i mnoze razy 100 zeby zrobic z tego normalne procenty
discount = ((previous_price - current_price) / previous_price) * 100

# sprawdzam czy znizka to co najmniej 10 procent
if discount >= 10:
    # jak siadlo to wale zachete do kupna i ucinam przecinki uzywajac inta zeby pokazalo rowne 30% 
    print(f'Kup produkt!! Cena produktu obniżona o {int(discount)}%')