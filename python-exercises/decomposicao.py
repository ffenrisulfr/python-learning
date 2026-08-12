# Este programa realiza a decomposição de um número inteiro em seus fatores primos.
# O usuário é solicitado a digitar um número inteiro, e o programa utiliza uma função chamada decompor para encontrar e exibir os fatores primos desse número.
numerador = int(input("Digite um número inteiro: "))

# A função decompor recebe um número inteiro como argumento e realiza a decomposição em fatores primos.
def decompor(num):
    divisor = 2 # Inicializamos o divisor com 2, que é o menor número primo. A decomposição em fatores primos começa a partir do menor primo e vai aumentando até que o número seja completamente fatorado.
    
    # Enquanto o número for maior que 1, o loop continua. O objetivo é dividir o número pelo divisor atual até que ele não seja mais divisível por esse divisor, e então passar para o próximo divisor.
    while num > 1:
        # Se o número for divisível pelo divisor atual, significa que encontramos um fator primo. O programa imprime o numerador e o fator da divisão, e então divide o número pelo divisor para continuar a decomposição.
        if num % divisor == 0:            
            print(f"numerador: {num}, e o fator da divisão: {divisor}")
            if num == divisor:
                print(f"O número {num} é primo, pois o fator da divisão é {divisor}")
                
            num = num // divisor
        else:
            divisor += 1 # Se o número não for divisível pelo divisor atual, o programa incrementa o divisor em 1 para testar o próximo número. Isso garante que todos os fatores primos sejam encontrados, pois o loop continuará até que o número seja completamente fatorado em 1.

print(decompor(numerador))

# Futuramente, podemos aprimorar o programa para lidar com números negativos, zero e um, que não possuem fatores primos. Além disso, podemos adicionar uma função para verificar se o número é primo antes de iniciar a decomposição, tornando o programa mais eficiente.
# Além disso, podemos implementar uma função para armazenar os fatores primos em uma lista ou dicionário, permitindo que o usuário visualize todos os fatores primos de uma vez, em vez de apenas imprimir cada fator à medida que é encontrado, ou possibilitar a visualização em ordem exponencial, como por exemplo: 2^3 * 3^1 * 5^2, que representa a decomposição do número 180 em fatores primos.