# Este programa calcula o fatorial de um número e a combinação entre dois números, utilizando a fórmula C(n,k) = n! / (k!(n-k)!)
# Começamos solicitando ao usuário que digite dois números, N e P, que serão utilizados para calcular o fatorial e a combinação
num = int(input("Digite um valor N: "))
num2 = int(input("Digite um valor P: "))

# Função de validação para verificar se os números são válidos para o cálculo da combinação
def validation(n, k):
    # A função verifica se n e k são válidos para o cálculo da combinação. Se n ou k forem menores que 0, ou se n for menor que k, a função retorna False, indicando que os números não são válidos. Caso contrário, retorna True. Pois, na matemática, a combinação C(n,k) só é definida para n >= 0, k >= 0 e n >= k.
    if n < 0 or k < 0 or n < k:        
        return False
    return True

# Função para calcular o fatorial de um número
def fatorial(n):
    fat_result = 1 # Inicializamos a variável fat_result com 1, pois o fatorial de 0 é 1 e multiplicar por 1 não altera o resultado
    if n < 0: return f"erro: impossível prosseguir se {n} é menor que 0" # Se n for menor que 0, a função retorna uma mensagem de erro
    while n > 0: # Enquanto n for maior que 0, multiplicamos fat_result por n e decrementamos n em 1
        fat_result *= n # Multiplicamos fat_result por n, acumulando o resultado do fatorial. Como o n é decrementado a cada iteração, isso equivale a calcular n! = n * (n-1) * (n-2) * ... * 1
        n -= 1
    return fat_result # A função retorna o resultado do fatorial de n

# Função para calcular a combinação entre dois números
def combination(n, k):
    # Se a validação retornar False, a função retorna uma mensagem de erro informando que um dos números é menor que 0 ou que N é menor que K
    if not validation(n, k):
        return f"erro: um dos números digitados é menor que 0 e/ou há uma situação no qual N é menor que K [números digitados: {n}, {k}]"
    
    # Se a validação retornar True, a função calcula a combinação utilizando a fórmula C(n,k) = n! / (k!(n-k)!)
    comb_result = fatorial(n) // (fatorial(k) * fatorial(n-k))
    return comb_result    # A função retorna o resultado da combinação entre n e k

# Exibimos os resultados do fatorial e da combinação para os números fornecidos pelo usuário
print(f"o fatorial de {num} é: {fatorial(num)}")
print(f"o fatorial de {num2} é: {fatorial(num2)}")
print(f"a combinação entre {num} e {num2} é: {combination(num, num2)}")