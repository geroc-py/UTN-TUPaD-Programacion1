
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



# Ejercicio 2 - Acceso al Campus y Menú Seguro

usuario = "alumno"
clave = "python123"

intentos = 0
acceso_concedido = False

while intentos < 3:
    print(f"Intento {intentos+1}/3")
    usuario_intento = input("Usuario: ")
    clave_intento = input("Clave: ")
    if usuario_intento == usuario and clave_intento == clave:
        print("Ha ingresado con éxito!")
        acceso_concedido = True
        break
    else:
        print("Error: credenciales inválidas. Intente nuevamente.\n")
        intentos+=1

if not acceso_concedido:
    print("Su cuenta ha sido bloqueada. Cantidad máxima de intentos superada. Comuníquese con un administrador del sitio.")
else:
    while True:
        print("\nMenú de selección: ")
        print("\n1) Estado  2) Cambio de clave  3) Mensaje motivacional  4) Salir")
        opcion = input("Ingrese una opción: ")
        if not opcion.isdigit():
            print("Por favor, ingrese una opción válida.")
            continue

        opcion =int(opcion)

        if opcion < 1 or opcion > 4:
            print("Opción fuera de rango.")
            print("Por favor, ingrese una opción válida.")
            continue
        if opcion == 1:
            print("Estado: Inscripto.")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) < 6:
                print("La clave debe tener al menos 6 dígitos.")
            else:
                confirmacion_clave = input("Confirme nueva clave: ")
                if nueva_clave == confirmacion_clave:
                    clave = nueva_clave
                    print("Su clave ha sido cambiada con éxito.")
                else:
                    print("Error. Las claves no coinciden.")
        elif opcion == 3:
            print("'No dejes para mañana lo que puedas hacer hoy.' - Mafalda. ")
        elif opcion == 4:
            print("Saliendo del sistema...")
            print("Hasta la próxima!")
            break


# Ejercicio 3 - Agenda de turnos con nombres

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1= ""
martes2= ""
martes3= ""

nombre_operador = input("Ingrese el nombre del operador: ")
print(f"Bienvenido/a, {nombre_operador}!")

while True:
    print("\n SISTEMA DE TURNOS ")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Por favor, seleccione una opción: ")

    if not opcion.isdigit():
        print("Error. Seleccione un número (1/5): ")
        continue

    opcion =int(opcion)

    if opcion == 1:
        dia = input("Elija el día: 1) Lunes, 2) Martes: ")
        if dia == "1":
            paciente = input("Nombre del paciente: ")
            if not paciente.isalpha():
                print("Por favor, ingrese un nombre válido.")
            elif paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya está tiene un turno registrado.")
            elif lunes1 == "": lunes1 = paciente; print("El turno 1 ha sido asignado.")
            elif lunes2 == "": lunes2 = paciente; print("El turno 2 ha sido asignado.")
            elif lunes3 == "": lunes3 = paciente; print("El turno 3 ha sido asignado.")
            elif lunes4 == "": lunes4 = paciente; print("El turno 4 ha sido asignado.")
            else:
                print("No hay turnos disponibles para el lunes.")
        elif dia == "2":
            paciente = input("Nombre del paciente: ")
            if not paciente.isalpha():
                print("Por favor, ingrese un nombre válido.")
            elif paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya está tiene un turno registrado.")
            elif martes1 == "": martes1 = paciente; print("El turno 1 ha sido asignado.")
            elif martes2 == "": martes2 = paciente; print("El turno 2 ha sido asignado.")
            elif martes3 == "": martes3 = paciente; print("El turno 3 ha sido asignado.")
            else:
                print("No hay turnos disponibles para el martes.")
    elif opcion == 2:
        dia = input("Elija el día: 1) Lunes, 2) Martes: ")
        paciente = input("Nombre del paciente a cancelar: ")
        encontrado = False
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""; encontrado = True
            elif lunes2 == paciente: lunes2 = ""; encontrado = True
            elif lunes3 == paciente: lunes3 = ""; encontrado = True
            elif lunes4 == paciente: lunes4 = ""; encontrado = True
        elif dia == "2":
            if martes1 == paciente: martes1 = ""; encontrado = True
            elif martes2 == paciente: martes2 = ""; encontrado = True
            elif martes3 == paciente: martes3 = ""; encontrado = True
        if encontrado:
            print("El turno ha sido cancelado con éxito.")
        else:
            print("Paciente no encontrado.")
    elif opcion == 3:
        dia = input("Elija el día: 1) Lunes, 2) Martes: ")
        if dia == "1":
            print(f"1: {lunes1 if lunes1 != "" else "(libre)"}")
            print(f"2: {lunes2 if lunes2 != "" else "(libre)"}")
            print(f"3: {lunes3 if lunes3 != "" else "(libre)"}")
            print(f"4: {lunes4 if lunes4 != "" else "(libre)"}")
        elif dia == "2":
            print(f"1: {martes1 if martes1 != "" else "(libre)"}")
            print(f"2: {martes2 if martes2 != "" else "(libre)"}")
            print(f"3: {martes3 if martes3 != "" else "(libre)"}")
    elif opcion == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes+=1
        if lunes2 != "": ocupados_lunes+=1
        if lunes3 != "": ocupados_lunes+=1
        if lunes4 != "": ocupados_lunes+=1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes+=1
        if martes2 != "": ocupados_martes+=1
        if martes3 != "": ocupados_martes+=1

        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres.")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres.")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es el lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es el martes.")
        else:
            print("Empate en la cantidad de turnos dados.")
    elif opcion == 5:
        print("Cerrando sistema. Hasta la próxima!")
        break


# Ejercicio 4 - Abrir la cerradura

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo = ""
contador_anti_spam = 0

agente = ""
while not agente.isalpha():
    agente = input("Ingrese el nombre del agente: ")

print(f"Bienvenido Agente {agente}, abra las 3 cerraduras antes de agotar sus recursos: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("La alarma ha sido activada. Seguridad está en camino.")
        break
    print(f"Estado actual:\nEnergía: {energia}\nTiempo: {tiempo}\nCerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {"Activada" if alarma else "Desactivada"}\nCódigo: {codigo}")

    print("\nMENU DE ACCIONES")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = ""
    while not opcion.isdigit():
        opcion = input("Seleccione una opción: ")
    opcion = int(opcion)

    if opcion == 1:
        energia-=20
        tiempo-=2
        contador_anti_spam+=1
        if contador_anti_spam == 3:
            alarma = True
            print("La cerradura ha sido forzada 3 veces seguidas. La alarma ha sido activada.")
        else:
            if energia < 40:
                print("Estás cansado. Riesgo de alarma en aumento.")
                riesgo = ""
                while not riesgo.isdigit():
                    riesgo = input("Elija un número de seguridad (1/3): ")
                if int(riesgo) == 3:
                    alarma = True
                    print("Falló tu técnica. La alarma ha sido activada.")
            if not alarma:
                cerraduras_abiertas+=1
                print("Cerradura abierta exitosamente.")
    elif opcion == 2:
        energia-=10
        tiempo-=3
        contador_anti_spam = 0

        print("Hackeo en progreso...")
        for i in range(1,5):
            print(f"Paso {i}/4...")
            codigo+="G"
        if len(codigo) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas+=1
            print("Código hackeado exitosamente. Una cerradura ha sido abierta.")
    elif opcion == 3:
        tiempo-=1
        contador_anti_spam = 0
        descanso = 15
        if alarma:
            print("La alarma no te permite descansar (-10 de energía extra).")
            descanso-=10
        energia+=descanso
        if energia > 100:
            energia = 100
        print(f"Descansaste. Tu energía actual es: {energia}")
    else:
        print("Opción inválida. Perdiste tiempo.")
        tiempo-=1

if cerraduras_abiertas >= 3:
    print(f"MISIÓN EXITOSA. El agente {agente} logró abrir la bóveda.")
elif energia <= 0:
    print("MISIÓN FALLIDA. Te quedaste sin energía.")
elif tiempo <= 0:
    print("MISIÓN FALLIDA. Te quedaste sin tiempo.")
else:
    print("MISIÓN FALLIDA. Fin del juego.")


# Ejercicio 5 - Escape Room: La Arena del Gladiador

nombre_gladiador = ""
while not nombre_gladiador.isalpha():
    nombre_gladiador = input("Nombre del Gladiador: ")
    if not nombre_gladiador.isalpha():
        print("Error: Solo se permiten letras.")

vida_gladiador=100
vida_enemigo=100
pociones_vida=3
danio_base_gladiador=15
danio_base_enemigo=12
turno_gladiador= True

while vida_enemigo>0 and vida_gladiador>0:
    if turno_gladiador:
        print("Turno gladiador")
        print(f"El gladiador {nombre_gladiador} tiene {vida_gladiador} puntos de vida")
        print(f"El enemigo tiene {vida_enemigo} puntos de vida")
        print(f"Te quedan {pociones_vida} pociones de vida")
        while True:
            print("""
                - 1. Ataque pesado
                - 2. Ráfaga veloz
                - 3. Curar
                """)
            opcion=input("Elegí una opción de acción: ")
            match opcion:
                case "1":
                        vida_enemigo -= danio_base_gladiador
                        print(f"Atacaste al enemigo por {danio_base_gladiador} puntos de daño")
                        if vida_enemigo<20:
                            vida_enemigo=vida_enemigo-danio_base_gladiador*1.5
                            print(f"Atacaste al enemigo por {danio_base_gladiador*1.5} puntos de daño")
                        break
                case "2":
                    for i in range(3):
                        vida_enemigo=vida_enemigo-5
                        print("Golpe conectado por 5 de daño")
                    break
                case "3":
                    if pociones_vida>0:
                        vida_gladiador=vida_gladiador+30
                        pociones_vida=pociones_vida-1
                    else:
                        print("No quedan pociones :(")
                        print("Perdiste el turno")
                    break
                case _:
                    print("Valor inválido.")
        turno_gladiador=False
    else:
        vida_gladiador=vida_gladiador-danio_base_enemigo
        print("El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador=True

if vida_gladiador>0:
    print(f"VICTORIA, {nombre_gladiador} ha ganado la batalla")
else:
    print("DERROTA, fuiste superado por el enemigo.")

