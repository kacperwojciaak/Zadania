# tygodniowy plan posilkow na 7 dni w ukladzie sniadanie obiad kolacja
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

# funkcja zwraca nazwe dnia tygodnia dla numeru od 1 do 7
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

# funkcja laczy posilki z wybranego dnia w jeden tekst oddzielony przecinkami
def day_meal_plan(meal_plan, day_number):
    # wyciagam liste posilkow dla danego dnia odejmujac 1 od numeru dnia
    meals = meal_plan[day_number - 1]
    # sklejam elementy listy w jeden ciag znakow
    return ", ".join(meals)

# drukuje naglowek planu posilkow
print("WEEKLY MEAL PLAN (Breakfast, Lunch, Dinner)")
print("==========================")

# lece petla po numerach dni od 1 do 7 i wypisuje dzien oraz jego menu
for day in range(1, 8):
    print(f"{weekday(day)}: {day_meal_plan(meal_plan, day)}")