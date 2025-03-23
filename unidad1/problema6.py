# Un individuo, animado por su interés en las plantas, se dirige a un vivero con la intención de
# enriquecer su jardín. En el vivero, una variedad de flores está a la venta, cada una con un precio distintivo. 
# El individuo ha apartado una suma determinada de dinero para destinar a su adquisición, aunque la cifra precisa no se menciona en este momento. 
# ¿Cuántas flores podrá llevar consigo basándose en el presupuesto que ha estimado?


# Análisis:

'''
Inicio
   |
   |---> Solicitar: lista de precios de las flores
   |
   |---> Solicitar: presupuesto disponible
   |
   |---> Ordenar los precios de las flores de menor a mayor
   |
   |---> Inicializar: flores_compradas = 0
   |
   |---> Mientras haya flores disponibles y presupuesto suficiente:
   |         |
   |         |---> Verificar si el presupuesto es suficiente para la siguiente flor
   |         |         |
   |         |         |---> Si el presupuesto es suficiente:
   |         |         |         |
   |         |         |         |---> Restar el precio de la flor del presupuesto
   |         |         |         |
   |         |         |         |---> Incrementar flores_compradas
   |         |         |
   |         |         |---> Si no es suficiente:
   |         |               |
   |         |               |---> Terminar el proceso de compra
   |
   |---> Mostrar: número de flores compradas
   |
Fin
'''

# Supongamos que las flores tienen los siguientes precios: [10, 5, 7, 3, 8] y el presupuesto es de 20.

def cantidad_flores(precios, presupuesto):
    # Ordenar la lista de precios de flores de menor a mayor
    precios.sort()
    
    flores_compradas = 0
    
    # Recorrer la lista de precios y comprar las flores mientras haya presupuesto
    for precio in precios:
        if presupuesto >= precio:
            presupuesto -= precio
            flores_compradas += 1
        else:
            break  # Si no hay suficiente presupuesto para la siguiente flor, terminamos
    
    return flores_compradas

# Ejemplo de uso
precios = [10, 5, 7, 3, 8]  # Lista de precios de las flores
presupuesto = 20  # El presupuesto disponible

resultado = cantidad_flores(precios, presupuesto)
print(f"El número de flores que se puede comprar es: {resultado}")
