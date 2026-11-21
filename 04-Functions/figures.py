# laduje modul zolwia
import turtle

# funkcja rysuje kwadrat o podanej dlugosci boku
def draw_square(length):
    # petla powtarza sie 4 razy bo kwadrat ma 4 boki
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

# funkcja rysuje trojkat rownoboczny o podanej dlugosci boku
def draw_triangle(length):
    # petla powtarza sie 3 razy a zolw skreca o 120 stopni zeby zamknac trojkat
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)

# funkcja rysuje prostokat o bokach a i b
def draw_rectangle(length_a, length_b):
    # powtarzam dwa razy zestaw dluzszy bok i krotszy bok
    for i in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)