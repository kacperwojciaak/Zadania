# wrzucam swoje dane
name = 'Kacper'
surname = 'Wójciak'

# wyciągam inicjał imienia. nawiasy kwadratowe z zerem [0] 
# mówią komputerowi: "daj mi pierwszą literę z tego słowa"
print(name[0])

# to samo dla nazwiska. też biorę pierwszą literę
print(surname[0])

# a tu wersja pro, jak to zrobić w jednej linijce używając f-stringa.
# po prostu wrzucam obie wycięte litery obok siebie do klamerek
print(f'My initials are: {name[0]}{surname[0]}')