# pobieram wymiary z klawiatury. 
# od razu owijam inputa w funkcję int(), żeby w jednej szybkiej linijce 
# pobrać tekst i od razu przerobić go na twardą liczbę do liczenia
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

# liczę objętość - po prostu mnożę wszystkie trzy boki przez siebie
volume = a * b * c

# liczę pole powierzchni. prostopadłościan ma 3 pary takich samych ścian.
# liczę pole każdej z trzech różnych ścian (a*b, a*c, b*c), dodaję je do siebie 
# i całość mnożę razy 2 (bo każda ściana ma swojego bliźniaka naprzeciwko)
surface_area = 2 * (a * b + a * c + b * c)

# wypluwam wynik z użyciem f-stringa, żeby gładko wkleić zmienne w klamerkach
print(f'The volume of a cuboid is {volume}')
print(f'The surface area of a cuboid is {surface_area}')