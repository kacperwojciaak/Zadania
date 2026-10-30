# Program obliczający objętość i pole powierzchni sześcianu

# Wczytujemy bok sześcianu jako tekst z klawiatury
cube_side_string = input('Enter cube side: ')

# Funkcja int() zamienia tekst (ciąg znaków) na liczbę całkowitą, żeby można było liczyć
cube_side = int(cube_side_string)

# Obliczamy objętość sześcianu (bok do potęgi 3, czyli a * a * a)
cube_volume = cube_side ** 3

# Obliczamy pole powierzchni sześcianu (sześć ścian o polu a * a)
cube_surface_area = 6 * (cube_side ** 2)

# Wypisujemy wynik objętości
print(f'The volume of a cube with side {cube_side} is {cube_volume}')

# Wypisujemy wynik pola powierzchni
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')