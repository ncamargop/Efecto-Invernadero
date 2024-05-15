import turtle
import random

window = turtle.Screen()
window.setup(width=800, height=600)
window.title("Simulación del efecto invernadero")
window.bgcolor("lightblue")
foton_rojo = 0

def superficie():
    pasto = turtle.Turtle()
    pasto.speed(0)
    pasto.color("green")
    pasto.penup()
    pasto.goto(-400, -200)
    pasto.begin_fill()
    for i in range(2):
        pasto.forward(800)
        pasto.right(90)
        pasto.forward(200)
        pasto.right(90)
    pasto.end_fill()

def crear_fotones():
    foton = turtle.Turtle()
    foton.shape("circle")
    foton.color("yellow")
    foton.penup()
    foton.goto(random.randint(-400, 400), 300) 
    foton.dy = -90  
    foton.dx = random.uniform(-5, 5)  
    return foton


def crear_gas(x, y):
    gas_inv = turtle.Turtle()
    gas_inv.shape("square")
    gas_inv.color("gray")
    gas_inv.penup()
    gas_inv.goto(x, y)
    return gas_inv


def main(nivel_cont):
    global foton_rojo
    fotones = []
    gases_inv = []
    superficie()

    for i in range(nivel_cont):
        x = random.randint(-400, 400)
        y = random.randint(100, 150)
        gas_inv = crear_gas(x, y)
        gases_inv.append(gas_inv)

    counter_colision = {}


    temp_box = turtle.Turtle()
    temp_box.hideturtle()
    temp_box.penup()
    temp_box.goto(0, 250)
    temp_box.color("black")
    temp_box.write("Temperatura: 20°C", align="center", font=("Arial", 16, "normal"))

    while True:
        foton = crear_fotones()
        fotones.append(foton)
        for foton in fotones:
            foton.sety(foton.ycor() + foton.dy) 
            foton.setx(foton.xcor() + foton.dx)  
            if foton.ycor() < -200:
                foton.dy *= -1
                foton.color("orange")
            for gas in gases_inv:
                if foton.distance(gas) < 35:
                    counter_colision[(foton, gas)] = counter_colision.get((foton, gas), 0) + 1
                    if counter_colision[(foton, gas)] >= 2:
                        foton.color("red")
                        foton.goto(gas.position())
                        fotones.remove(foton)
                        foton_rojo += 1
                        cambiar_temp(temp_box)
                        break
        window.update()


def cambiar_temp(temp_box):
    global foton_rojo
    new_temp = 20 + 0.1 * foton_rojo
    temp_box.clear()
    temp_box.write("Temperatura: {:.1f}°C".format(new_temp), align="center", font=("Arial", 16, "normal"))


nivel_cont = turtle.numinput("Nivel de gases invernaderos", "Ingrese un valor entre 1 y 5 de nivel de contaminación (1 es bajo):", default=20)
main(int(nivel_cont*5))
turtle.mainloop()
