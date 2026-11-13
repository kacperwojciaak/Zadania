# definiujemy zmienna z tytulem filmu
movie = "The Lord of the Rings: The Return of the King"

# len liczy wszystkie znaki lacznia ze spacjami i dwukropkami
print('Number of characters: ', len(movie))

# zamieniamy wszystkie litery na wielkie
print(movie.upper())

# zamieniamy wszystkie litery na male
print(movie.lower())

# liczymy ile razy wystepuje mala litera e
print(movie.count('e'))

# szukamy na ktorej pozycji zaczyna sie slowo Lord
print(movie.find("Lord"))

# szukamy slowa dragon 
print(movie.find("dragon"))