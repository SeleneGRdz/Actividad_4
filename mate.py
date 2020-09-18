from math import pi

class Mate:
    def cuadrado(self, x:int):
        print("El area del cuadrado es: " +str(x * x))

    def triangulo(self, x:int, y:int):
        print("El area del triángulo es: "+str((x * y) / 2))

    def circulo(self, x:int):
        print("El area del círculo es: "+str(pi * x ** 2))

    
