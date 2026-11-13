# krece petla od 1 do 30 uzywajac range
# range dociaga do tej drugiej liczby 
for i in range(1, 31):
    
    # najpierw musze sprawdzic najtrudniejszy warunek czyli czy dzieli sie przez 3 i 5 jednoczesnie
    # uzywam modulo czyli znaczka procent zeby sprawdzic czy reszta z dzielenia to rowne zero
    if i % 3 == 0 and i % 5 == 0:
        print("BINGO")
        
    # jesli powyzsze nie siadlo to sprawdzam czy dzieli sie tylko przez sama 3
    elif i % 3 == 0:
        print("THREE")
        
    # jesli trojka tez nie weszla to sprawdzam czy dzieli sie tylko przez sama 5
    elif i % 5 == 0:
        print("FIVE")
        
    # jak kompletnie zaden warunek wyzej nie pasuje to wypluwam na ekran po prostu sama liczbe
    else:
        print(i)