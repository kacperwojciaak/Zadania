# tworze tablice z lista polskich imion
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# zakladam na start ze pierwsze imie na liscie jest najdluzsze
longest_name = names[0]

# lece petla po kazdym imieniu i porownuje jego dlugosc
for name in names:
    # jesli obecne imie ma wiecej znakow niz zapamietane to je podmieniam
    if len(name) > len(longest_name):
        longest_name = name

# wypisuje wszystkie imiona z tablicy w jednej linii
print("Names:", end=" ")
for name in names:
    print(name, end=" ")
print()

# wyswietlam najdluzsze znalezione imie
print("Longest name:", longest_name)