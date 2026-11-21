# tworze krotke z podanymi liczbami
numbers = (10, 20, 30, 40, 50)

# odwracam krotke za pomoca wycinka z krokiem -1
reversed_numbers = numbers[::-1]

# zamieniam liczby na tekst i sklejam je przecinkami do wyswietlenia
print("Tuple:", ",".join([str(n) for n in numbers]))
print("Reverse order:", ",".join([str(n) for n in reversed_numbers]))