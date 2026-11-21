# laduje modul zolwia i moj wlasny modul z figurami
import turtle
import figures

# ustawiam okno i kolor tla
window = turtle.Screen()
window.bgcolor("lightgreen")

# ustawiam predkosc rysowania zolwia
turtle.speed(5)

# rysuje pierwszy kwadrat na srodku
figures.draw_square(100)

# podnosze pisak przesuwam zolwia w lewy gorny rog i rysuje drugi kwadrat
turtle.penup()
turtle.goto(-200, 150)
turtle.pendown()
figures.draw_square(60)

# przesuwam zolwia w prawy gorny rog i rysuje pierwszy trojkat
turtle.penup()
turtle.goto(150, 150)
turtle.pendown()
figures.draw_triangle(100)

# przesuwam zolwia nizej i rysuje drugi trojkat
turtle.penup()
turtle.goto(150, -50)
turtle.pendown()
figures.draw_triangle(70)

# przesuwam zolwia w lewy dolny rog i rysuje pierwszy prostokat
turtle.penup()
turtle.goto(-200, -100)
turtle.pendown()
figures.draw_rectangle(120, 60)

# przesuwam zolwia na sam dol i rysuje drugi prostokat
turtle.penup()
turtle.goto(-50, -200)
turtle.pendown()
figures.draw_rectangle(80, 40)

# chowam strzalke zolwia i zatrzymuje okno zeby nie zniknelo od razu
turtle.hideturtle()
window.mainloop()