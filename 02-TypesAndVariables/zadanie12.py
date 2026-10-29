### # Program obliczający populację i procentowy udział na półkulach #

# Zdefiniowanie całkowitej liczby ludności świata
total = 8000000000

# Zdefiniowanie liczby ludzi na półkuli północnej
north = 7200000000

# Obliczenie liczby ludzi na półkuli południowej (całość minus półkula północna)
south = total - north

# Wyświetlenie podstawowych informacji o populacji
print("World population: ", total)
print("Northern Hemisphere: ", north)

# Obliczenie i wydrukowanie procentu dla półkuli północnej
north_percentage = (north / total) * 100
print(f"Northern Hemisphere in %: {north_percentage:.2f}%")

# Wyświetlenie informacji dla półkuli południowej
print("Southern Hemisphere: ", south)

# Obliczenie i wydrukowanie procentu dla półkuli południowej
south_percentage = (south / total) * 100
print(f"Southern Hemisphere in %: {south_percentage:.2f}%")