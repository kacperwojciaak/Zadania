### # Program wyświetlający dane osobowe oraz obliczający przyszły wiek przy użyciu f-stringów #

# Przypisujemy wartości do zmiennych
name = "Adam"
age = 20
height = 175

# 1. Wyświetlamy imię, wiek oraz wzrost w jednym zdaniu za pomocą f-stringa
print(
    f"My name is {name}. I am {age} years old, and my height is {height} cm."
)

# 2. Obliczamy wiek za 6 lat bezpośrednio wewnątrz klamer {} f-stringa
print(f"In 6 years I will be {age + 6} years old.")