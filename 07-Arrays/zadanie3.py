# funkcja zwraca nazwe dnia tygodnia dla podanego numeru od 1 do 7
def weekday(n):
    # tworze liste z nazwami wszystkich dni tygodnia po kolei
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # odejmuje 1 od numeru dnia bo indeksy na liscie licza sie od zera
    return weekdays[n - 1]

# wypisuje nazwy dni dla numerow 1 4 oraz 7
print(weekday(1))
print(weekday(4))
print(weekday(7))