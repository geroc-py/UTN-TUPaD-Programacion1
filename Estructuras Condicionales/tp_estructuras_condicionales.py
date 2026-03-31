# Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    pass


# Ejercicio 2
nota = int(input("Ingrese su calificación: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Ejercicio 3
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par.")


# Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Usted es un niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto/a joven")
else:
    print("Usted es un adulto/a")


#Ejercicio 5
clave = input("Ingrese una contraseña: ")
if len(clave) >= 8 and len(clave) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# Ejercicio 6
consumo_mensual = int(input("Ingrese su consumo mensual de energía eléctrica (en kWh): "))
if consumo_mensual < 150:
    print("Consumo bajo")
elif consumo_mensual >= 150 and consumo_mensual <= 300:
    print("Consumo medio")
elif consumo_mensual > 300 and consumo_mensual <= 500:
    print("Consumo alto")
elif consumo_mensual > 500:
    print("Consumo alto")
    print("Considere medidas de ahorro energético.")


# Ejercicio 7
palabra = input("Ingrese una palabra o frase: ")
if palabra [-1].lower() in "aeiou":
    print(palabra + "!")
else:
    print(palabra)


# Ejercicio 8
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese una opción (del 1 al 3): "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())


# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Richter Muy leve (imperceptible)")
elif magnitud < 4:
    print("Richter Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Richter Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Richter Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Richter Muy fuerte (puede causar daños significativos)")
else:
    print("Richter Extremo (puede causar graves daños a gran escala)")


# Ejercicio 10
hemisferio = input("Ingrese el hemisferio en el cual se encuentra (N/S): ").upper()
mes = int(input("Ingrese el mes actual (1-12): "))
dia = int(input("Ingrese el día actual: "))
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en invierno")
    else:
        print("Usted se encuentra en verano")
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en primavera")
    else:
        print("Usted se encuentra en otoño")
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en verano")
    else:
        print("Usted se encuentra en invierno")
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Usted se encuentra en otoño")
    else:
        print("Usted se encuentra en primavera")
