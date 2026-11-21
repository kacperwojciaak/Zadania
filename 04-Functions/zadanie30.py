# funkcja sumuje wszystkie cyfry ktore powtarzaja sie w liczbie
def f(number):
    # zamieniam liczbe na tekst zeby latwo liczyc ile razy wystepuje kazda cyfra
    text = str(number)
    # ustawiam sume na zero przed startem
    total = 0
    
    # lece petla po kazdej cyfrze po kolei
    for digit in text:
        # sprawdzam czy ta cyfra wystepuje w calym napisie wiecej niz raz
        if text.count(digit) > 1:
            # zamieniam znak z powrotem na liczbe i dodaje do sumy
            total += int(digit)
            
    return total

# sprawdzam funkcje na przykladach z polecenia
print(f(1027))
print(f(230335))
print(f(513553007))