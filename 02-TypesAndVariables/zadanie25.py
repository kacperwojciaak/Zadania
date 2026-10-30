# Program wyciągający szczegółowe informacje z tekstu za pomocą wycinków (slicing)

employee = "Mr. John May, born on 1998-02-16"

# Wyciągamy imię "John" (znaki od indeksu 4 do 8 włącznie, bo koniec przedziału nie jest wliczany)
name = employee[4:8]

# Wyciągamy nazwisko "May" (indeksy od 9 do 12)
surname = employee[9:12]

# Wyciągamy datę urodzenia na samym końcu (od indeksu 22 do końca)
birth_date = employee[22:]

# Składamy inicjały z pierwszych liter imienia i nazwiska
initials = name[0] + surname[0]

# Wypisujemy wyniki w osobnych wierszach
print(f'Name: {name}')
print(f'Surname: {surname}')
print(f'Born: {birth_date}')
print(f'Initials: {initials}')