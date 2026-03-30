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