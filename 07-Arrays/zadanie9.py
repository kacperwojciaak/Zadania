# tworze dwie listy gdzie pozycje kategorii odpowiadaja kwotom wydatkow
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# znajduje najwyzsza kwote wsrod wszystkich wydatkow
max_expense = max(expenses)

# sprawdzam pod ktorym indeksem na liscie lezy ta najwyzsza kwota
max_index = expenses.index(max_expense)

# wyciagam nazwe kategorii z tego samego indeksu i wyswietlam wynik
most_expensive_category = categories[max_index]
print("Most expensive category:", most_expensive_category)
print("Amount spent:", max_expense)