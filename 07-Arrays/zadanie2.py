# tworze liste z poczatkowymi wartosciami
arr = [1, 2, 3, 4, 5]
print('Array:', arr)

# odejmuje 1 od pierwszego elementu z indeksu 0
arr[0] -= 1
print('Array:', arr)

# dodaje 4 do ostatniego elementu tablicy
arr[-1] += 4
print('Array:', arr)

# wyliczam srodkowy indeks i mnoze ten element przez 2
mid = len(arr) // 2
arr[mid] *= 2
print('Array:', arr)