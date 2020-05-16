"""
Ejercicio 2
"""

password = "contraseña"

passwordUsuario = input("Introduzca la contraseña: ").lower()

if password == passwordUsuario:
    print("El password es correcto😀")
else:
    print("El password no coincide")