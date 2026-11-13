# program do zamiany wartości dwóch zmiennych za pomocą zmiennej pomocniczej
x = 7
y = 34
z = 0  # dodatkowa, pomocnicza zmienna

# pokazuję jak wyglądało przed zamianą
print("Before swapping: x=", x, "y=", y)

# robię swap (zamianę) wartości przy użyciu zmiennej pomocniczej z
z = x  # chowam siódemkę do zeszyny (z ma teraz 7)
x = y  # przypisuję trzydzieści cztery do x
y = z  # wyciągam siódemkę z z i daję do y

# pokazuję wynik po zamianie
print("After swapping: x=", x, "y=", y)