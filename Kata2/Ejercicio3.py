"""
Ejercicio3
"""
edad = int(input("Introduce tu edad: "))

if edad < 4:
    print("La vida te sonrie, pasas gratis 😀")
elif edad >=4 and edad <18:
    print("El precio de la entrada es: 5€ 😐")
else:
    print("La vida es dura, la entrada es: 10€ 😑")