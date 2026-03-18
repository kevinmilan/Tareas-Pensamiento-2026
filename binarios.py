opcion = 0

while opcion != 4:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Convertir decimal a maya")
    print("3. Convertir decimal a binario")
    print("4. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Hola, bienvenido")

    elif opcion == 2:
        print("Módulo de conversión de decimal a maya")
        num = int(input("Ingresa un número decimal: "))

        if num == 0:
            print("0 = concha (cero maya)")
        else:
            # Primero contamos cuántos niveles tendrá
            temp = num
            niveles = 0

            while temp > 0:
                temp = temp // 20
                niveles += 1

            # Ahora imprimimos de arriba hacia abajo
            for i in range(niveles - 1, -1, -1):
                divisor = 20 ** i
                valor = num // divisor
                num = num % divisor

                if valor == 0:
                    print("0")
                else:
                    barras = valor // 5
                    puntos = valor % 5

                    linea = ""

                    # imprimir barras (—)
                    for j in range(barras):
                        linea += "—"

                    # imprimir puntos (*)
                    for j in range(puntos):
                        linea += "*"

                    print(linea)

    elif opcion == 3:
        print("Módulo de conversión de decimal a binario")
        num = int(input("Ingresa un número decimal: "))

        if num == 0:
            print("0 base 2 = 0")
        else:
            binario = ""
            original = num

            while num > 0:
                residuo = num % 2
                binario = str(residuo) + binario
                num = num // 2

            print(f"{original} base 10 = {binario} base 2")

    elif opcion == 4:
        print("Saliendo del programa")

    else:
        print("Opción no válida")