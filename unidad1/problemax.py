
# Generar un patrón de figuras geométricas aleatorias

import random
import turtle

def generar_patron(num_figuras, tamano_maximo):
    for _ in range(num_figuras):
        tipo_figura = random.choice(['circulo', 'cuadrado', 'triangulo'])
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        tamano = random.randint(10, tamano_maximo)
        
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        if tipo_figura == 'circulo':
            turtle.circle(tamano)
        elif tipo_figura == 'cuadrado':
            for _ in range(4):
                turtle.forward(tamano)
                turtle.right(90)
        elif tipo_figura == 'triangulo':
            for _ in range(3):
                turtle.forward(tamano)
                turtle.right(120)

# Configuración inicial de Turtle
turtle.speed(0)
turtle.bgcolor("white")
generar_patron(10, 100)  # Generar un patrón con 10 figuras de tamaño máximo 100
turtle.done()
