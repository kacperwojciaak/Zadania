# na poczatek ustawiam czas prania na zero zeby miec do czego dodawac minuty w zaleznosci od wyborow
total_washing_time = 0

# pobieram od usera glowny program czyli co bedzie prane
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')

# pytam czy chce dodatkowe plukanie i wirowanie i zapisuje sobie odpowiedzi
extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

# sprawdzam co wpisal przy glownym programie i wrzucam odpowiednia liczbe minut do mojej zmiennej
if program == 'j':
    total_washing_time += 40
elif program == 'u':
    total_washing_time += 70
elif program == 's':
    total_washing_time += 20

# patrze czy gosc zaznaczyl yes przy dodatkowym plukaniu
# jak tak to dorzucam do ogolnego czasu 15 minut
if extra_rinse == 'y':
    total_washing_time += 15

# robie dokladnie to samo dla wirowania tylko ze to zajmuje 9 minut wiec dodaje 9
if extra_spin == 'y':
    total_washing_time += 9

# wypluwam calosc na ekran z uzyciem f-stringa zeby wstawic ta obliczona zmienna prosto w tekst
print(f'Całkowity czas prania: {total_washing_time} minut')