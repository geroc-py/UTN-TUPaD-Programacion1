# Ejercicio 1 - Caja del Kiosco

nombre = input("Ingrese su nombre: ")

while not nombre.isalpha():
    print("Solo es posible ingresar letras.")
    nombre = input("Por favor, ingrese su nombre: ")

cantidad_productos = input("Ingrese la cantidad de productos: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("La cantidad de productos debe ser mayor a cero.")
    cantidad_productos = input("Por favor, ingrese la cantidad de productos: ")

cantidad_prod_entero = int(cantidad_productos)

total_sin_dscto = 0
total_con_dscto = 0

for i in range(1, cantidad_prod_entero+1):
    precio_producto = input(f"Producto {i} - Precio: ")

    precio_prod_entero = int(precio_producto)

    descuento = input(f"Producto {i}, tiene descuento? (S/N): ").strip().lower()

    while descuento not in ["s", "n"]:
            print("Por favor, ingrese 'S' o 'N'.")
            descuento = input(f"Producto {i}, tiene descuento? (S/N): ").strip().lower()

    total_sin_dscto+=precio_prod_entero

    if descuento == "s":
        precio_final = precio_prod_entero * 0.9
    else:
        precio_final = precio_prod_entero

    total_con_dscto+=precio_final

ahorro = total_sin_dscto - total_con_dscto
promedio = total_con_dscto / cantidad_prod_entero

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad_prod_entero}")
print(f"Total sin descuento: ${total_sin_dscto}")
print(f"Total con descuento: ${total_con_dscto:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")