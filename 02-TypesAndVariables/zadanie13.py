# Oceny z poszczególnych przedmiotów. 
# Usunąłem hasz (#) przed math, żeby odblokować zmienną, bo inaczej komputer ją ignorował.
math = 5
art = 4
music = 5

# Wywaliłem apostrofy wokół trójki. To ma być twarda liczba do liczenia, a nie tekst.
history = 3

# Liczę średnią. Dodałem nawiasy, żeby najpierw dodać wszystkie oceny, a dopiero potem podzielić całość przez 4.
# Poprawiłem też literówki w nazwach przedmiotów (było mat, Art, muzic).
average = (math + art + music + history) / 4

# Wypisuję wynik. Poprawiłem cudzysłowy na równe i literówkę w zmiennej (było averege).
print("Average grade is", average)