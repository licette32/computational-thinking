# Un individuo joven y ansioso, en medio de la vorágine de las demandas académicas, se encuentra confrontado con la perentoria tarea de administrar
# su limitado tiempo disponible para acometer variadas materias de estudio.
# Cada asignatura en su currículum impone un requisito inequívoco de tiempo diario a ser consagrado. El joven se encuentra frente a una ristra de
# ineludibles obligaciones que deben ser satisfactorias. La cantidad de tiempo
# semanal de la que dispone para estos fines asciende a 20 horas en total.

# Dada esta compleja situación, el individuo se plantea: 
# ¿Cómo, en efecto, podría dividir su limitado tiempo de manera óptima para obtener el mayor rendimiento en su preparación académica?

# Datos
total_horas = 20
materias = ["Matemáticas", "Física", "Química"]
tiempo_diario = [2, 5, 4]  # Tiempo diario requerido para cada materia

# Cálculo: Total de tiempo requerido
tiempo_total_requerido = sum(tiempo_diario)

# Calcular proporción de tiempo por materia
tiempo_distribuido = [(materia, (tiempo/tiempo_total_requerido) * total_horas) for materia, tiempo in zip(materias, tiempo_diario)]

# Mostrar distribución de tiempo
for materia, tiempo in tiempo_distribuido:
    print(f"Para {materia}, dedicarás {tiempo:.2f} horas.")
