# stan pierwszego przelacznika (wylaczony lub wlaczony)
light_switch1 = True

# stan drugiego przelacznika
light_switch2 = True

# zeruje zmienna liczaca palace sie zarowki
bulbs_on = 0

# jesli pierwszy przelacznik jest wlaczony to dodaje jedna zarowke
if light_switch1:
    bulbs_on += 1

# jesli drugi przelacznik jest wlaczony to dodaje dwie zarowki
if light_switch2:
    bulbs_on += 2

# wyswietlam ile lacznie zarowek sie swieci
print(f'Number of bulbs illuminating the house: {bulbs_on}')