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