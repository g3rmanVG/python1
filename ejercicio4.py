''''Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.'''

products = input("Enter the products separeted by commas: ")

products_list = products.split(',')

for product in products_list:
    print(product.strip())
