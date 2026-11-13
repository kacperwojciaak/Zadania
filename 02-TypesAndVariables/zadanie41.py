import random
computer = random.randint(1, 6)
you = int(input("Zgadnij wynik rzuti od 1 do 6: "))
you_won = (computer == you)
print(f"you won: {you_won}")