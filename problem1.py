#Pensamiento algoritmico

# Reentrenando al ratón
#Un ratón e laboratorio ha sido entrenado para salir de un laberinto siguiendo
#una serie de tubos numerados. El ratón ha sido entrenado para salir por el
#tubo número cinco, pero los científicos han modificado el laberinto y ahora
#el ratón no puede salir por el tubo número cinco.

#Los científicos están buscando la forma de entrenar nuevamente al ratón para
#que, ingresando por cualquier tubo, salga siempre por el número cinco, ¿podés escribir un algoritmo que resuelva el problema?


def construir_laberinto():
    # Representaremos el laberinto como un diccionario en donde las claves serán los tubos y los valores serám listas de conexiones
    return {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: []  # El punto final donde está el queso
    }

def encontrar_camino(laberinto, punto_inicio, punto_final):
    visitados = set()
    camino = []
    
    def dfs(nodo):
        if nodo in visitados:
            return False
        visitados.add(nodo)
        camino.append(nodo)
        
        if nodo == punto_final:
            return True
        
        for vecino in laberinto.get(nodo, []):
            if dfs(vecino):
                return True
        
        camino.pop()
        return False
    
    if dfs(punto_inicio):
        return camino
    return None

# Creamos el laberinto con las conexiones
laberinto = construir_laberinto()

# Probamos desde cada tubo
for entrada in range(1, 6):
    camino = encontrar_camino(laberinto, entrada, 5)
    if camino:
        print(f"El ratón debe entrar por el tubo {entrada} para llegar al queso. Ruta: {camino}")
