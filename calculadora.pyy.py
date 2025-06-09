num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

while True:
    print("""
Seleccione una opción:
1 - Sumar
2 - Restar
3 - Multiplicar
4 - Dividir
5 - Sumar 3 valores
""")
    valor = int(input("Elige una opción: "))

    if valor == 1:
        print("La suma es:", num1 + num2)
        break
    elif valor == 2:
        print("La resta es:", num1 - num2)
        break
    elif valor == 3:
        print("La multiplicación es:", num1 * num2)
        break
    elif valor == 4:
        if num2 != 0:
            print("La división es:", num1 / num2)
        else:
            print("No se puede dividir por cero.")
        break
    elif valor == 5:
        print("La suma de los tres valores es:", num1 + num2 + num3)
        break
    else:
        print("Opción incorrecta. Intenta de nuevo.")