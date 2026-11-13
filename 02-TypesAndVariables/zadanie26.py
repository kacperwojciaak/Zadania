# pobieram numer z klawiatury. 
# nie będę tego numeru mnożył ani dzielił, tylko ciął nożyczkami na kawał
phone = input('Enter phone number: ')

# tnę tekst na trzy równe kawałki po 3 znaki.
#prawa liczba w nawiasie nie wchodzi do cięcia
czesc_1 = phone[0:3]  # bierze indeksy 0, 1, 2
czesc_2 = phone[3:6]  # bierze indeksy 3, 4, 5
czesc_3 = phone[6:9]  # bierze indeksy 6, 7, 8 (czyli do samego końca)

# wypluwam na ekran, ładując wycięte kawałki do klamerek w f-stringu 
# i wstawiając między nie zwykłe, twarde myślniki
print(f'Phone number: {czesc_1}-{czesc_2}-{czesc_3}')