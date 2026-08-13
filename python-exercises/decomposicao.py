# Este programa é uma nova versão do programa de decomposição em fatores primos, que agora inclui a capacidade de lidar com números negativos e operações usando listas. Vamos na ordem de construção do programa:
# OBS.: Anteriormente, tinhamos apenas a função decompor, que retornava uma lista de fatores primos. Agora, adicionamos a função agrupamento, que agrupa os fatores primos e suas quantidades em uma lista de listas!

# 1. Perguntamos ao usuário para digitar um número inteiro, que será armazenado na variável numerador.
numerador = int(input("Digite um número inteiro: "))

# 2. A função atribur_valor verifica se o número é negativo e retorna True ou False. Porém, ela só será chamada em dois casos: na função decompor e na função formatar, para que possamos lidar com números negativos de forma adequada.
def atribur_valor():
    return numerador < 0
 
# 3. A função decompor recebe um número inteiro e retorna uma lista de fatores primos. Ela utiliza um loop while para dividir o número pelo menor divisor possível (começando em 2) até que o número seja reduzido a 1. Se o número for negativo, ele é convertido para positivo antes da decomposição. Mas, calma, vou explicar cada parte do código para melhor compreensão:            
def decompor(num):
    fator = [] # Criamos uma lista vazia chamada fator, que será usada para armazenar os fatores primos do número.
    divisor = 2 # Inicializamos a variável divisor com o valor 2, que é o menor número primo. Essa variável será usada para verificar se o número é divisível por ela.
    
    # Nesse "if" verificamos se o número é igual a zero. Se for, retornamos uma lista vazia, pois o número 0 não possui fatores primos.
    if num == 0:
        return []
    
    # Já nesse "if" verificamos se o número é negativo. Se for, multiplicamos o número por -1 para torná-lo positivo, pois a decomposição em fatores primos é feita apenas com números positivos. Este é um dos casos ditos anteriormente.
    if atribur_valor():
        num *= -1
    
    # Melhoramos a função anterior e separamos cada função por responsabilidade. Agora, a função decompor é responsável apenas por decompor o número em fatores primos. Como de praxe, utilizamos um loop while para continuar dividindo o número pelo menor divisor possível até que o número seja reduzido a 1. Se o número for divisível pelo divisor, adicionamos o divisor à lista de fatores e dividimos o número por ele. Caso contrário, incrementamos o divisor em 1 e continuamos o processo. Isso garante que todos os fatores primos do número sejam encontrados e armazenados na lista fator. Pense nela como n, n + 1, n + 2, n + 3, n + 4, n + 5, n + 6, n + 7, n + 8, n + 9, n + 10, n + 11, n + 12, n + 13, n + 14, n + 15, n + 16, n + 17, n + 18, n + 19, n + 20 e assim por diante.
    while num > 1:
        # Só conseguimos encontrar os fatores se o resto da divisão do número pelo divisor for igual a zero. Se for, adicionamos o divisor à lista de fatores e dividimos o número por ele. Caso contrário, incrementamos o divisor em 1 e continuamos o processo.
        if num % divisor == 0:    
            num = num // divisor
            fator.append(divisor)
        else: divisor += 1
    return fator # Retornamos a lista de fatores primos encontrados.

# 4. A função agrupamento recebe uma lista de fatores primos e retorna uma lista de listas, onde cada sublista contém um fator primo e sua quantidade de ocorrência na lista original. Ela utiliza um loop for para percorrer a lista de fatores e agrupar os fatores iguais em sublistas. Se a lista de fatores estiver vazia, a função retorna uma lista vazia.
def agrupamento(fator):
    
    # Se a lista de fatores estiver vazia, retornamos uma lista vazia novamente, pois não há fatores para agrupar.
    if not fator:
        return []
       
    lista = [] # Criamos uma lista vazia chamada lista, que será usada para armazenar as sublistas de fatores primos e suas quantidades.
    quantidade = 0 # Inicializamos a variável quantidade com o valor 0, que será usada para contar a quantidade de ocorrências de cada fator primo na lista de fatores.
    verificando = fator[0] # Inicializamos a variável verificando com o primeiro elemento da lista de fatores, que será usada para comparar os fatores primos e agrupar os iguais em sublistas.
    
    # Nesse loop for, percorremos a lista de fatores e verificamos se o fator atual é igual ao fator que estamos verificando. Se for, incrementamos a quantidade em 1. Caso contrário, adicionamos uma sublista contendo o fator que estávamos verificando e sua quantidade à lista de sublistas, e atualizamos a variável verificando com o novo fator atual. No final do loop, adicionamos a última sublista à lista de sublistas.
    # A lógica por trás seria representar a ideia de numero + quantas vezes ele se repete, por exemplo: 2^3 * 3^2 * 5^1, onde o número 2 se repete 3 vezes, o número 3 se repete 2 vezes e o número 5 se repete 1 vez.
    for item in fator:
        if verificando != item:
            lista.append([verificando, quantidade])
            quantidade = 1
            verificando = item
        else:
            quantidade += 1
    lista.append([verificando, quantidade])   
    return lista # Retornamos a lista de sublistas contendo os fatores primos e suas quantidades.
    
# Calma que já estamos terminando!
# 5. A função formatar recebe uma lista de sublistas contendo os fatores primos e suas quantidades, e retorna uma string formatada representando a decomposição em fatores primos do número original. Ela utiliza um loop for para percorrer a lista de sublistas e criar uma lista de strings representando cada fator primo e sua quantidade. Se a quantidade for igual a 1, apenas o fator primo é adicionado à lista de strings. Caso contrário, o fator primo é adicionado à lista de strings com o símbolo de exponenciação (^) seguido da quantidade. No final, a lista de strings é unida em uma única string usando o operador de multiplicação (*) como separador.
def formatar(lista):
    bloco = [] # Criamos uma lista vazia chamada bloco, que será usada para armazenar as strings representando cada fator primo e sua quantidade. Sim, de novo, estamos utilizando uma lista para armazenar as strings, pois é mais eficiente do que concatenar strings diretamente.
    
    # Se a lista de sublistas estiver vazia, retornamos uma string informando que o número não possui fatores primos. Caso contrário, percorremos a lista de sublistas e verificamos a quantidade de cada fator primo. Se a quantidade for igual a 1, apenas o fator primo é adicionado à lista de strings. Caso contrário, o fator primo é adicionado à lista de strings com o símbolo de exponenciação (^) seguido da quantidade.
    if not lista:
        return f"{numerador} não possui fatores primos"
    for elemento in lista:
        if elemento[1] == 1:
            bloco.append(f"{elemento[0]}")
        else:
            bloco.append(f"{elemento[0]}^{elemento[1]}")
    
    # Lembra que falamos sobre a função atribur_valor? Pois é, aqui ela é chamada novamente para verificar se o número original era negativo. Se for, adicionamos um sinal de menos antes da string formatada, caso contrário, apenas retornamos a string formatada.
    if not atribur_valor():
        mostrar = " * ".join(bloco)
    else:
        mostrar = "-(" + " * ".join(bloco) + ")"
           
    return mostrar # Retornamos a string formatada representando a decomposição em fatores primos do número original.

# Por fim, chamamos as funções decompor, agrupamento e formatar em sequência, passando o número digitado pelo usuário como argumento. O resultado final é armazenado na variável resultado e impresso na tela.
resultado = formatar(agrupamento(decompor(numerador)))
print(resultado)