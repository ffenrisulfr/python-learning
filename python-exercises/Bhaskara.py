# Este é um programa que calcula as raízes reais de uma equação do segundo grau utilizando a fórmula de Bhaskara.
# O programa solicita ao usuário os valores dos coeficientes A, B e C da equação ax² + bx + c = 0 e calcula suas raízes.
# Também trata casos especiais, como quando A é igual a zero (equação do primeiro grau) ou quando o delta é negativo
# (situação em que as raízes são complexas e não pertencem ao conjunto dos números reais).

import math  # importa operações matemáticas comuns

# Solicita ao usuário os coeficientes da equação
A = float(input("Valor de A: "))
B = float(input("Valor de B: "))
C = float(input("Valor de C: "))

# Função de Bhaskara adaptada ao Python
def bhaskara(a, b, c):
    # caso A seja 0, a equação deixa de ser do segundo grau e vira uma equação do primeiro grau (bx + c = 0)
    if a == 0:
        return "Não é uma equação do segundo grau"
    
    delta = b**2 - 4*a*c  # calcula o discriminante da equação (delta = b² - 4ac)

    # caso delta seja menor que 0, as raízes são complexas e não são calculadas pelo programa
    if delta < 0:
        return "Não há raízes reais"
    
    x1 = (-b + math.sqrt(delta)) / (2*a)  # calcula a primeira raiz da equação
    x2 = (-b - math.sqrt(delta)) / (2*a)  # calcula a segunda raiz da equação
    
    return x1, x2  # retorna os valores das duas raízes da equação

print(bhaskara(A, B, C))  # informa ao usuário os valores das raízes x1 e x2 obtidas