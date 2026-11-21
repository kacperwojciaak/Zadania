# laduje moj modul do ukrywania numeru karty
import card_mask

# wpisuje przykladowy szesnastocyfrowy numer karty jako tekst
card = "5290312400019022"

# wywoluje funkcje z modulu i zapisuje zamaskowany numer
masked_card = card_mask.hide(card)

# wypisuje gotowy wynik na ekranie
print(masked_card)