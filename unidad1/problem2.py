#Pensamiento algoritmico y descomposición

#Problema 2
# Heriberto necesita llegar a su casa y usa un automóvil autónomo (que está en un estadio rudimentario de desarrollo, muy lejos de la
# IA deseada por sus realizadores). El automóvil está programado con solo tres instrucciones:
# I: girá 90° a la izquierda.
# D: girá 90° a la derecha.
# A: avanzá hasta el próximo cruce.

# PREGUNTA: Utilizando las tres instrucciones anteriores, ¿podés escribir un algoritmo que guíe al personaje a su casa por el camino más corto
# (en cantidad de instrucciones)?


# PISTA
# Como ej, compartimos un algoritmo que lleva al automóvil desde el origen hasta el pino solitario: A, A, A, I, A, A, A.

# Algoritmo para llegar a casa:
# 1. Avanzar hasta el primer cruce.
# 2. Seguir avanzando hasta el segundo cruce.
# 3. Seguir avanzando hasta el tercer cruce.
# 4. Girar a la izquierda en el cruce.
# 5. Avanzar hasta el siguiente cruce.
# 6. Girar a la derecha en el cruce.
# 7. Avanzar hasta el siguiente cruce.
# 8. Girar a la izquierda en el cruce.
# 9. Avanzar hasta la casa.


def llegar_a_casa():
    instrucciones = ["A", "A", "A", "I", "A", "D", "A", "I", "A"]
    for instruccion in instrucciones:
        print(f"Ejecutando: {instruccion}")

llegar_a_casa()
