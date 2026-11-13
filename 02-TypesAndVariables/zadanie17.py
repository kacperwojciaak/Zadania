# komenda input() zatrzymuje program i czeka, aż wpiszę coś z klawiatury, 
# a potem wrzuca to do zmiennej first_name
first_name = input('Enter your first name: ')

# to samo dla nazwiska, program znowu staje i czeka na mój wpis
last_name = input('Enter your last name: ')

# sklejam imię z nazwiskiem (dodaję też pustą spację w cudzysłowie w środku, żeby się nie zlały)
full_name = first_name + ' ' + last_name

# wypluwam na ekran używając f-stringa (f przed cytatem), żeby łatwo wkleić zmienne w klamerki
print(f'Your first name is {first_name} and your last name is {last_name}')

# to samo, tylko wypluwam gotową zmienną ze sklejonym wszystkim naraz
print(f'And your full name is {full_name}')