### # Program do zamiany wartości dwóch zmiennych z użyciem zmiennej pomocniczej #
x = 7
y = 34
z = 0  # Dodatkowa, pomocnicza zmienna

print("Before swapping: x=", x, "y=", y)

# Zamiana wartości z użyciem zmiennej z
z = x  # z przechowuje chwilowo wartość x (czyli 7)
x = y  # x przyjmuje wartość y (czyli 34)
y = z  # y przyjmuje zapisaną w z pierwotną wartość x (czyli 7)

print("After swapping: x=", x, "y=", y)