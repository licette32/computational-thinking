# Problema 4

# Un joven, entusiasta de los dulces, se dirige a una tienda en busca de satisfacer su antojo. Cada caramelo en esta tienda tiene
# un costo de $50. El joven ha destinado una suma precisa de $2600 para invertir en su dulce
# selección. ¿Cuántos caramelos específicamente podrá adquirir con esta cantidad de dinero?


# Datos
monto = 2600
precio_caramelo = 50

# Cálculo
cantidad_caramelos = monto // precio_caramelo  # División entera

# Mostrar resultado
print(f"Con ${monto}, puedes comprar {cantidad_caramelos} caramelos.")