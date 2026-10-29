### # Poprawiony program obliczający średnią ocenę studenta #

# Przypisujemy poprawne wartości do zmiennych (zmieniamy 'math' na 'math_grade', aby unikać konfliktów)
math_grade = 5
art = 4
music = 5

# Konwertujemy tekst '3' na liczbę całkowitą (int)
history = int('3')

# Obliczamy średnią: używamy nawiasów, żeby najpierw zsumować wszystkie oceny, a dopiero potem podzielić przez 4
average = (math_grade + art + music + history) / 4

# Wyświetlamy wynik, poprawiając cudzysłowy oraz literówkę w nazwie zmiennej
print(f"Average grade is {average}")