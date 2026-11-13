# komenda input czeka aż wpiszę długość boku i chowa to do zmiennej.
cube_side_string = input('Enter cube side: ')


cube_side = int(cube_side_string)

# liczę objętość sześcianu: wzór to bok do sześcianu, czyli (a * a * a)
cube_volume = cube_side * cube_side * cube_side

# liczę pole powierzchni: sześcian ma 6 takich samych ścian o polu (a * a)
cube_surface_area = 6 * (cube_side * cube_side)

# wypluwam wynik z użyciem f-stringa, pakując wyliczone zmienne prosto w klamerki
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')