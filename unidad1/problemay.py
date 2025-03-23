
# Generador de Patrones para Colorear

import random
import pygame

# Inicialización de Pygame
pygame.init()

# Definición de colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Dimensiones de la ventana (lienzo)
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Generador de Patrones para Colorear")

def generar_numero_aleatorio(minimo, maximo):
    """Genera un número entero aleatorio dentro de un rango."""
    return random.randint(minimo, maximo)

def generar_circulo(tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo):
    """Genera las propiedades de un círculo aleatorio."""
    radio = generar_numero_aleatorio(tamaño_minimo, tamaño_maximo)
    x = generar_numero_aleatorio(radio, ancho_lienzo - radio)
    y = generar_numero_aleatorio(radio, alto_lienzo - radio)
    return {"tipo": "circulo", "radio": radio, "centro": (x, y)}

def generar_cuadrado(tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo):
    """Genera las propiedades de un cuadrado aleatorio."""
    lado = generar_numero_aleatorio(tamaño_minimo, tamaño_maximo)
    x = generar_numero_aleatorio(0, ancho_lienzo - lado)
    y = generar_numero_aleatorio(0, alto_lienzo - lado)
    return {"tipo": "cuadrado", "lado": lado, "top_left": (x, y)}

def generar_triangulo(tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo):
    """Genera las propiedades de un triángulo aleatorio."""
    # Generar vértices de forma más controlada para que se vea como un triángulo
    x1 = generar_numero_aleatorio(50, ancho_lienzo - 50)
    y1 = generar_numero_aleatorio(50, alto_lienzo - 50)
    base = generar_numero_aleatorio(tamaño_minimo, tamaño_maximo)
    altura = generar_numero_aleatorio(tamaño_minimo, tamaño_maximo)
    x2 = x1 + base
    y2 = y1
    x3 = generar_numero_aleatorio(min(x1, x2), max(x1, x2))
    y3 = y1 - altura
    return {"tipo": "triangulo", "puntos": [(x1, y1), (x2, y2), (x3, y3)]}

def generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo):
    """Genera una lista de figuras geométricas para el patrón."""
    patron = []
    for _ in range(num_figuras):
        tipo = random.choice(tipos_figuras)
        if tipo == "circulo":
            patron.append(generar_circulo(tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo))
        elif tipo == "cuadrado":
            patron.append(generar_cuadrado(tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo))
        elif tipo == "triangulo":
            patron.append(generar_triangulo(tamaño_minimo, tamaño_maximo, ancho_lienzo, alto_lienzo))
    return patron

def dibujar_patron(pantalla, patron):
    """Dibuja el patrón en la pantalla."""
    pantalla.fill(BLANCO)  # Fondo blanco para colorear
    for figura in patron:
        if figura["tipo"] == "circulo":
            pygame.draw.circle(pantalla, NEGRO, figura["centro"], figura["radio"], 2)  # Borde negro
        elif figura["tipo"] == "cuadrado":
            pygame.draw.rect(pantalla, NEGRO, (figura["top_left"][0], figura["top_left"][1], figura["lado"], figura["lado"]), 2)
        elif figura["tipo"] == "triangulo":
            pygame.draw.polygon(pantalla, NEGRO, figura["puntos"], 2)
    pygame.display.flip()

def main():
    """Función principal del programa."""
    num_figuras = 10
    tipos_figuras = ["circulo", "cuadrado", "triangulo"]
    tamaño_minimo = 20
    tamaño_maximo = 100

    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
    dibujar_patron(pantalla, patron_actual)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    # Generar un nuevo patrón al presionar la barra espaciadora
                    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                    dibujar_patron(pantalla, patron_actual)
                elif evento.key == pygame.K_UP:
                    num_figuras += 1
                    print(f"Número de figuras: {num_figuras}")
                    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                    dibujar_patron(pantalla, patron_actual)
                elif evento.key == pygame.K_DOWN and num_figuras > 1:
                    num_figuras -= 1
                    print(f"Número de figuras: {num_figuras}")
                    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                    dibujar_patron(pantalla, patron_actual)
                elif evento.key == pygame.K_LEFT and tamaño_minimo > 5:
                    tamaño_minimo -= 5
                    print(f"Tamaño mínimo: {tamaño_minimo}")
                    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                    dibujar_patron(pantalla, patron_actual)
                elif evento.key == pygame.K_RIGHT and tamaño_maximo < min(ANCHO, ALTO) // 2:
                    tamaño_maximo += 5
                    print(f"Tamaño máximo: {tamaño_maximo}")
                    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                    dibujar_patron(pantalla, patron_actual)
                elif evento.key == pygame.K_c:
                    tipos_disponibles = ["circulo", "cuadrado", "triangulo"]
                    tipo_a_agregar = random.choice(tipos_disponibles)
                    if tipo_a_agregar not in tipos_figuras:
                        tipos_figuras.append(tipo_a_agregar)
                        print(f"Tipos de figuras ahora incluyen: {tipos_figuras}")
                        patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                        dibujar_patron(pantalla, patron_actual)
                elif evento.key == pygame.K_v and len(tipos_figuras) > 1:
                    tipo_a_eliminar = random.choice(tipos_figuras)
                    tipos_figuras.remove(tipo_a_eliminar)
                    print(f"Tipos de figuras ahora incluyen: {tipos_figuras}")
                    patron_actual = generar_patron(num_figuras, tipos_figuras, tamaño_minimo, tamaño_maximo, ANCHO, ALTO)
                    dibujar_patron(pantalla, patron_actual)

        # Se pueden agregar más controles para ajustar los tipos de figuras, etc.

    pygame.quit()

if __name__ == "__main__":
    main()