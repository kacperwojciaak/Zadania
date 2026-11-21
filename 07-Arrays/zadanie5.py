# tworze liste z nazwami popularnych gier
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sortuje liste alfabetycznie przy uzyciu wbudowanej funkcji sorted
sorted_games = sorted(computer_games)

# ustawiam indeks startowy na zero dla petli while
i = 0

# pętla dziala dopoki indeks jest mniejszy od liczby gier na liscie
while i < len(sorted_games):
    # wypisuje numer pozycji od 1 i nazwe gry z danego indeksu
    print(f"{i + 1}. {sorted_games[i]}")
    # podbijam licznik o 1 zeby przejsc do kolejnego elementu
    i += 1