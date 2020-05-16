"""
Ejercicio 1: Barras de pan
Precio 3.49€
Descuento: 60%
"""

precio = 3.49
descuento = 0.4
precioDescuento = precio * descuento

numeroBarras = int(input("Numero de barras vendidas: "))

print("Precio habitual: " + str(precio))
print("Descuento: " + str(precioDescuento))
print("Coste final: " + str(numeroBarras * precioDescuento)+"€")