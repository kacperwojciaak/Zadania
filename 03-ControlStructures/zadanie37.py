# ustawiam sztywne limity na zmiennych zeby miec to tak jak dokladnie chcieli w zadaniu
limit_predkosci_min = 40
limit_predkosci_max = 140

# pobieram z klawiatury ile koles leci i rzutuje na inta zeby moc to latwo porownywac z limitami
predkosc_samochodu = int(input('Wprowadź prędkość samochodu: '))

# sprawdzam czy predkosc jest ponizej minimalnej albo czy przekracza maksymalna uzywajac operatora or
if predkosc_samochodu < limit_predkosci_min or predkosc_samochodu > limit_predkosci_max:
    
    # jak zlamal ktorys z limitow to wale na ekran to ostrzezenie z wykrzyknikami
    print('Ostrzeżenie: nieprawidłowa prędkość samochodu!!')
    
# tu by mozna bylo dodac else jak jedzie przepisowo ale w poleceniu chcieli tylko komunikat jak zlamie zasady