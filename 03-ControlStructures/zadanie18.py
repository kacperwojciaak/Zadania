# zeruje zmienna do ktorej bedzie dodawana suma
sum = 0

# przechodze petla w zakresie od 5 do 10 wlacznie
for i in range(5, 11):
    # dodaje kolejna liczbe do sumy uzywajacy operatora plus rowna sie
    sum += i

# wyswietlam wynik zsumowanych liczb
print(f'Sum is {sum}')