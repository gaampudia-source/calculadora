memoria = []

num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

valor = 0

while True:
    print("""Seleccione opcion
    1- Sumar
    2- Restar
    3- Multiplicar
    4- Dividir
    """)

    valor = int(input("Elige una opcion: "))

    if valor == 1:
        resultado = num1 + num2
        print("La suma es", resultado)
        memoria.append(resultado)
        break

    if valor == 2:
        resultado = num1 - num2
        print("La resta es", resultado)
        memoria.append(resultado)
        break

    if valor == 3:
        resultado = num1 * num2
        print("La multiplicacion es", resultado)
        memoria.append(resultado)
        break

    if valor == 4:
        resultado = num1 / num2
        print("La division es", resultado)
        memoria.append(resultado)
        break

    else:
        print("Opcion no valida")