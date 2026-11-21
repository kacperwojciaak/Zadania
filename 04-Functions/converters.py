# przelicza metry na centymetry
def m_to_cm(n):
    return n * 100

# przelicza centymetry na metry
def cm_to_m(n):
    return n / 100

# przelicza centymetry na cale (1 cal to 2.54 cm)
def cm_to_inches(n):
    return n / 2.54

# przelicza stopy i cale na centymetry (1 stopa to 30.48 cm a 1 cal to 2.54 cm)
def feet_inches_to_cm(feet, inches):
    return (feet * 30.48) + (inches * 2.54)

# blok testowy uruchamia sie tylko gdy odpalisz ten konkretny plik bezposrednio
if __name__ == "__main__":
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'100cm = {cm_to_inches(100):.2f} inches')
    print(f'5 feet 10 inches = {feet_inches_to_cm(5, 10)}cm')