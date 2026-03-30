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