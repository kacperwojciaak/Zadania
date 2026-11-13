# ustawiam nasz poprawny pin jako tekst zeby nie wcielo tego zera na poczatku
poprawny_pin = "0805"

# krece petla dokladnie trzy razy bo tyle mamy szans w bankomacie
for proba in range(3):
    
    # pobieram pin od uzytkownika i zostawiam go jako tekst
    podany_pin = input("Wprowadź kod PIN: ")
    
    # sprawdzam czy wpisany pin idealnie zgadza sie z naszym
    if podany_pin == poprawny_pin:
        print("Zalogowano pomyślnie")
        # uzywam break zeby natychmiast wyrwac sie z petli bo przeciez juz zgadl
        break
        
    # jak nie zgadl to wypluwam komunikat bledu i petla leci dalej do kolejnej proby
    else:
        print("Nieprawidłowy...")
        
# to else na samym dole jest podpiete do petli for a nie do ifa
# odpali sie tylko wtedy gdy petla zakreci sie trzy razy i ani razu nie wywali jej break
else:
    print("Niestety, Twoja karta płatnicza została zablokowana.")