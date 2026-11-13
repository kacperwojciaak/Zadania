# tworze liste znakow do sprawdzenia
znaki = ["a", "b", "z", "A", "B", "Z", "1", "=", "+", "€"]

# petla leci po kazdym znaku po kolei
for znak in znaki:
    # ord bierze znak i zamienia go na liczbe (kod)
    kod_znaku = ord(znak)
    
    # wypisujemy wynik na ekranie
    print(f"Znak {znak} ma kod numeryczny: {kod_znaku}")