'''Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

password = 'password123'

userPassword = input("Ingrese la contraseña: ")

if password == userPassword:
    print("Contraseña correcta!")
else:
    print("Contraseña incorrecta!")
