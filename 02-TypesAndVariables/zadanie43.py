# pobieram temperaturę w Celsjuszach od użytkownika i zamieniam na liczbę zmiennoprzecinkową
celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))

# przeliczam Celsjusze na kelwiny (dodając 273.15)
kelvin = celsius + 273.15

# przeliczam Celsjusze na Fahrenheity (według wzoru: C * 9/5 + 32)
fahrenheit = (celsius * 9/5) + 32

# wypisuję wyniki na ekran
print(f"Temperatura w kelwinach: {kelvin}")
print(f"Temperatura w Fahrenheicie: {fahrenheit}")