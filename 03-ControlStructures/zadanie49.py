# krece petla od 1 do 9 bo tyle mamy rzedow cyfr
for i in range(1, 10):
    
    # zamieniam obecna liczbe z petli na tekst za pomoca str
    # i mnoze ten tekst przez sama liczbe co sprawia ze np "3" powtarza sie 3 razy
    wzor = str(i) * i
    
    # wypisuje gotowy sklejony wzor do konsoli
    print(wzor)