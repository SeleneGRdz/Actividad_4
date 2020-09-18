from mate import Mate

m = Mate()

while True:
    print("\nActividad_4")
    print("1. Áreas de figuras")
    print("2. Signos zodiacáles")
    print("3. Calculo número e")
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
        pass

    elif op==3:
        pass
    elif op==4:
        break