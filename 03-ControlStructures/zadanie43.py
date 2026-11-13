# drukuje naglowek ankiety
print("ANKIETA")

# pobieram odpowiedz i od razu sprawdzam czy wpisano t zeby otrzymac wartosc logiczna true lub false
odp1 = input("Czy interesujesz się informatyką? (t/n): ") == 't'
odp2 = input("Czy lubisz grać w gry komputerowe? (t/n): ") == 't'
odp3 = input("Czy masz konto na Instagramie? (t/n): ") == 't'

# pusta linijka i naglowek wynikow zeby ladnie wygladalo
print("\n \nWYNIKI ANKIETY")

# sprawdzam co ma w sobie pierwsza zmienna zeby wypisac slowo tak lub nie
if odp1:
    print("Zainteresowanie informatyką: Tak")
else:
    print("Zainteresowanie informatyką: Nie")

# to samo dla drugiego pytania
if odp2:
    print("Granie w gry komputerowe: Tak")
else:
    print("Granie w gry komputerowe: Nie")

# i to samo dla trzeciego pytania
if odp3:
    print("Posiadanie konta na Instagramie: Tak")
else:
    print("Posiadanie konta na Instagramie: Nie")