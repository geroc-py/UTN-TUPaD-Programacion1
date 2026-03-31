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