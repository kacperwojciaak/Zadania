### # Program obliczający długość przekątnej prostokąta o bokach a i b #
import math

a = 5
b = 8

# Twierdzenie Pitagorasa: przekątna = pierwiastek z (a^2 + b^2)
diagonal = math.sqrt(a**2 + b**2)

print("Długość boku a:", a)
print("Długość boku b:", b)
print("Długość przekątnej prostokąta:", diagonal)