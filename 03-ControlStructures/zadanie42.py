# pobieram z klawiatury pierwsza liczbe i robie z niej inta zeby dalo sie na niej liczyc
x = int(input("x = "))

# pobieram druga liczbe i tez zamieniam na inta
y = int(input("y = "))

# sprawdzam czy punkt to sam srodek ukladu czyli same zera
if x == 0 and y == 0:
    print(f"Punkt P({x},{y}) znajduje się w położeniu (0,0)")

# jak x jest zerem to znaczy ze punkt lezy rowno na pionowej osi y
elif x == 0:
    print(f"Punkt P({x},{y}) leży na osi Y")

# jak y jest zerem to znaczy ze punkt lezy na poziomej osi x
elif y == 0:
    print(f"Punkt P({x},{y}) leży na osi X")

# obie liczby na plusie wiec to prawy gorny rog czyli pierwsza cwiartka
elif x > 0 and y > 0:
    print(f"Punkt P({x},{y}) leży w pierwszej ćwiartce układu współrzędnych")

# x na minusie a y na plusie wiec lewy gorny rog czyli druga cwiartka
elif x < 0 and y > 0:
    print(f"Punkt P({x},{y}) leży w drugiej ćwiartce układu współrzędnych")

# obie liczby na minusie wiec lewy dolny rog czyli trzecia cwiartka
elif x < 0 and y < 0:
    print(f"Punkt P({x},{y}) leży w trzeciej ćwiartce układu współrzędnych")

# x na plusie a y na minusie wiec prawy dolny rog czyli czwarta cwiartka
elif x > 0 and y < 0:
    print(f"Punkt P({x},{y}) leży w czwartej ćwiartce układu współrzędnych")