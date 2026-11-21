# funkcja liczy ile razy podana litera wystepuje w tekscie
def count_letter(text, letter):
    # ustawiam licznik na zero przed startem
    count = 0
    # przechodze petla przez kazdy znak w calym tekscie
    for char in text:
        # jak znak pasuje do szukanej litery to dodaje jeden do licznika
        if char == letter:
            count += 1
    return count