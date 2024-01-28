''''Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.'''

dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

if divisor == 0:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {dividend/divisor}")
