# Ejercicio 1
print("Hola Mundo!")


# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# Ejercicio 3
nombre = input("Mi nombre es: ")
apellido = input("Mi apellido es: ")
nombre_completo = nombre + apellido
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Vivo en: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")


# Ejercicio 4
import math

radio = float(input("Ingrese el radio: "))
area = math.pi * radio * radio
perimetro = 2 * math.pi * radio

print(f"El área del círculo es {area} y el perímetro es {perimetro}")


# Ejercicio 5
numero = int(input("Ingrese una cantidad de segundos: "))
horas = numero / 3600
print(f"{numero} segundos equivale a {horas} horas")


# Ejercicio 6
x = int(input("Ingrese un número: "))

print(f"Tabla del {x}: ")
print(f"{x} x 1 es" ,x * 1)
print(f"{x} x 2 es" ,x * 2)
print(f"{x} x 3 es" ,x * 3)
print(f"{x} x 4 es" ,x * 4)
print(f"{x} x 5 es" ,x * 5)
print(f"{x} x 6 es" ,x * 6)
print(f"{x} x 7 es" ,x * 7)
print(f"{x} x 8 es" ,x * 8)
print(f"{x} x 9 es" ,x * 9)
print(f"{x} x 10 es" ,x * 10)


# Ejercicio 7
x = int(input("Ingrese un número entero: "))
y = int(input("Ingrese otro número entero: "))

print(x * y)
print (x / y)
print (x + y)
print (x - y)


# Ejercicio 8
x = int(input("Ingrese su peso en kg: "))
y = float(input("Ingrese su altura en metros: "))
IMC = x / y ** 2

print(f"Su IMC es {IMC}")


# Ejercicio 9
x = int(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = 9/5 * x + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")


# Ejercicio 10
x = int(input("Ingrese un número: "))
y = int(input("Ingrese un número: "))
z = int(input("Ingrese un número: "))
promedio = (x + y + z) / 3

print(f"El promedio es {promedio}")
