import math

A = float(input("Valor de A: "))
B = float(input("Valor de B: "))
C = float(input("Valor de C: "))

def Bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    
    if(delta < 0):
        return "Não há raízes reais"  
    
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    
    return x1, x2

print(Bhaskara(A, B, C))