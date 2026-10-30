# Program obliczający objętość i pole powierzchni prostopadłościanu o bokach a, b i c

# Wczytujemy boki z klawiatury i od razu zamieniamy tekst na liczby całkowite za pomocą int()
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

# Obliczamy objętość prostopadłościanu (wzór: a * b * c)
cuboid_volume = a * b * c

# Obliczamy pole powierzchni całkowitej prostopadłościanu (wzór: 2*ab + 2*bc + 2*ac)
cuboid_surface_area = 2 * (a * b + b * c + a * c)

# Wypisujemy wyniki na ekranie
print(f'The volume of a cuboid with sides {a}, {b}, {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with sides {a}, {b}, {c} is {cuboid_surface_area}')