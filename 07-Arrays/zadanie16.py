# uklad miejsc na sali kinowej gdzie A to wolne a B to zajete
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]

# funkcja zlicza wszystkie miejsca na sali
def seats_total(seats):
    total = 0
    # dodaje dlugosc kazdego rzedu do sumy wszystkich miejsc
    for row in seats:
        total += len(row)
    return total

# funkcja zlicza wolne miejsca oznaczone litera A
def seats_available(seats):
    available = 0
    # przechodze po kazdym rzedzie i kazdym pojedynczym fotelu
    for row in seats:
        for seat in row:
            if seat == 'A':
                available += 1
    return available

# funkcja zlicza zajete miejsca oznaczone litera B
def seats_booked(seats):
    booked = 0
    # sprawdzam kazdy fotel po kolei i zliczam wystapienia litery B
    for row in seats:
        for seat in row:
            if seat == 'B':
                booked += 1
    return booked

# funkcja sprawdza czy konkretne miejsce jest wolne czy zajete
def seat_status(seats, row, place):
    # odejmuje 1 od rzedu i miejsca bo indeksy liczymy od zera
    if seats[row - 1][place - 1] == 'A':
        return "Available"
    else:
        return "Booked"

# wypisuje cale podsumowanie miejsc w kinie
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))