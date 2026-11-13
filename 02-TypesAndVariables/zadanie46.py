# pobieram odleglosc od klawiatury
distance = int(input("Enter distance in km: "))

# pobieram cene paliwa za litr
fuel_price = float(input("Enter fuel price per liter: "))

# pobieram ile auto pali na 100 km
fuel_consumption = float(input("Enter fuel consumption in liters per 100 km: "))

# licze ile ogolnie zuzyjemy paliwa (dystans podzielony na 100 razy spalanie)
total_fuel_consumption = (distance / 100) * fuel_consumption

# mnozec calkowite zuzycie paliwa przez jego cene, wychodzi calkowity koszt
total_cost = total_fuel_consumption * fuel_price

# wypisuje wyniki na ekranie
print("Total fuel consumption:", total_fuel_consumption, "liters")
print("Total cost:", total_cost, "PLN")