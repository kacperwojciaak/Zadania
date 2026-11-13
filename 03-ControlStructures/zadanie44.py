# pobieram liczbe od uzytkownika i robie z niej od razu inta
liczba = int(input("Wprowadź liczbę dziesiętną: "))

# robie sobie kopie tej liczby zeby na koniec moc ja wypisac w komunikacie
oryginal = liczba

# tutaj bede zbieral reszty z dzielenia jako tekst zeby na koncu je posklejac
wynik_binarny = ""

# jak ktos wpisze zero to od razu daje wynik zero zeby ominac to cale liczenie
if liczba == 0:
    wynik_binarny = "0"
else:
    # krece pętlą dopóki nasza liczba po dzieleniu nie zjedzie do zera
    while liczba > 0:
        # modulo 2 wyciaga mi reszte czyli to nasze 0 lub 1
        reszta = liczba % 2
        
        # dorzucam te reszte na sam poczatek mojego wyniku zeby zrobic to odwrotnie tak jak w poleceniu
        wynik_binarny = str(reszta) + wynik_binarny
        
        # dziele liczbe na pol bez reszty zeby miec nowy wynik do kolejnego kółka w pętli
        liczba = liczba // 2

# wypisuje caly gotowy tekst ze sklejonym wynikiem
print(f"{oryginal}(10) = {wynik_binarny}(2)")