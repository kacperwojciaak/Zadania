# wrzucam do listy wszystkie temperatury z polecenia zeby przetestowac je za jednym zamachem
temperatures = [33, 30, 8, 0, -2]

# lece petla po kazdej temperaturze z listy po kolei
for temp in temperatures:
    
    # wypisuje jaka temperature aktualnie sprawdzam zeby bylo czytelnie w konsoli
    print(f"Temperatura: {temp} C")
    
    # sprawdzam czy jest powyzej 35 stopni
    if temp > 35:
        print("Jest bardzo gorąco")
        
    # jak nie jest > 35 to sprawdzam czy jest powyzej 30
    elif temp > 30:
        print("Jest gorąco")
        
    # minimum 15 stopni czyli sprawdzam czy jest wieksze albo rowne 15
    elif temp >= 15:
        print("Jest ciepło")
        
    # co najmniej zero czyli wieksze lub rowne zero
    elif temp >= 0:
        print("Jest zimno")
        
    # jak wszystko wyzej odpada to logiczne ze musi byc ponizej zera
    else:
        print("Uwaga, mróz")
        
    # daje pusta linijke odstepu miedzy wynikami zeby sie nie zlewalo
    print()