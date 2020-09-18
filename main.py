from mate import Mate

m = Mate()

while True:
    print("\nActividad_4")
    print("1. Áreas de figuras")
    print("2. Signos zodiacales")
    print("3. Cálculo número e")
    print("4. Salir")
    op = int(input("Elige tu opción: "))

    if op==1:
        while True:
            print("\nÁreas de figuras")
            print("1. Cuadrado")
            print("2. Triángulo")
            print("3. Círculo")
            print("4. Salir")
            op = int(input("Elige tu opción: "))

            if op==1:
                x = int(input("Ingrese el radio del círculo: "))
                m.cuadrado(x)
            elif op==2:
                x = int(input("Ingrese la base del triángulo: "))
                y = int(input("Ingrese la altura del triángulo: "))
                m.triangulo(x,y)
            elif op==3:
                x = int(input("Ingrese el radio del círculo: "))
                m.circulo(x)
            elif op==4:
                break
    elif op==2:
        x = int(input("Ingresa tu dia de nacimiento[DD]: "))
        y = int(input("Ingresa tu mes de nacimiento[MM]: "))
        m.signo(x,y)

    elif op==3:
        x = int(input("Ingresa el límite: "))
        m.numero(x)

    elif op==4:
        break