from math import pi

class Mate:
    def cuadrado(self, x:int):
        print("El area del cuadrado es: " +str(x * x))

    def triangulo(self, x:int, y:int):
        print("El area del triángulo es: "+str((x * y) / 2))

    def circulo(self, x:int):
        print("El area del círculo es: "+str(pi * x ** 2))

    def signo(self, x:int, y:int):
        if (x>=20 and y==1) or (x<=19 and y==2):
            print("Tu signo es Acuario")
        elif (x>=19 and y==2) or (x<=20 and y==3):
            print("Tu signo es Piscis")
        elif (x>=21 and y==3) or (x<=19 and y==4):
            print("Tu signo es Aries")
        elif (x>=20 and y==4) or (x<=20 and y==5):
            print("Tu signo es Tauro")
        elif (x>=21 and y==5) or (x<=20 and y==6):
            print("Tu signo es Géminis")
        elif (x>=21 and y==6) or (x<=22 and y==7):
            print("Tu signo es Cáncer")
        elif (x>=23 and y==7) or (x<=22 and y==8):
            print("Tu signo es Leo")
        elif (x>=23 and y==8) or (x<=22 and y==9):
            print("Tu signo es Virgo")
        elif (x>=23 and y==9) or (x<=22 and y==10):
            print("Tu signo es Libra")
        elif (x>=23 and y==10) or (x<=21 and y==11):
            print("Tu signo es Escorpio")
        elif (x>=22 and y==11) or (x<=21 and y==12):
            print("Tu signo es Sagitario")
        elif (x>=22 and y==12) or (x<=19 and y==1):
            print("Tu signo es Capricornio")
    