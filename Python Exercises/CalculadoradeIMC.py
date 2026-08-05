# Este é um programa que calcula o Íncide de Massa Corporal (IMC) de uma pessoa com base em seu peso e altura. O IMC é uma medida utilizada para avaliar se uma pessoa está com peso adequado, abaixo do peso, sobrepeso ou obesidade.
# O programa solicita ao usuário os valores da altura e do peso, realiza o cálculo do IMC utilizando a fórmula IMC = peso / (altura * altura) e, em seguida, classifica o resultado de acordo com os padrões estabelecidos pela Organização Mundial da Saúde (OMS).

# Começamos solicitando ao usuário que insira seu peso em quilogramas e sua altura em metros.
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em centímetros: "))

# Chamamos a função calcular_imc passando os valores de peso e altura como argumentos. A função retorna o valor do IMC calculado, que é armazenado na variável imc.

def calcular_imc(peso, altura):
    imc = peso / (altura/100)**2 #Calcula o IMC utilizando a fórmula: IMC = peso / (altura * altura).
    return imc #Retorna: O valor do IMC calculado.

resultado_imc = calcular_imc(peso, altura)#Armazena o valor do IMC calculado na variável resultado_imc.

print("Seu IMC é: ", round(resultado_imc, 2)) #Exibe o valor do IMC formatado com duas casas decimais. round() é usado para arredondar o valor do IMC para duas casas decimais, tornando a apresentação mais legível e compreensível para o usuário.

if resultado_imc < 18.5: #Verifica se o IMC calculado é menor que 18.5, indicando que a pessoa está abaixo do peso.
    print("Você está abaixo do peso.") #Exibe a mensagem correspondente à classificação do IMC.
elif resultado_imc < 25: #Verifica se o IMC calculado está entre 18.5 e 24.9, indicando que a pessoa está com peso normal. Repare que não é necessário verificar se o IMC é maior ou igual a 18.5, pois essa condição já foi verificada no bloco anterior.
    print("Você está com peso normal.") #Exibe a mensagem correspondente à classificação do IMC.
elif resultado_imc < 30: #Verifica se o IMC calculado está entre 25 e 29.9, indicando que a pessoa está com sobrepeso.
    print("Você está com sobrepeso.") #Exibe a mensagem correspondente à classificação do IMC.
elif resultado_imc < 35: #Verifica se o IMC calculado é maior ou igual a 30, indicando que a pessoa está com obesidade grau I.
    print("Você está com obesidade grau I.") #Exibe a mensagem correspondente à classificação do IMC.
elif resultado_imc < 40: #Verifica se o IMC calculado é maior ou igual a 35, indicando que a pessoa está com obesidade grau II.
    print("Você está com obesidade grau II.") #Exibe a mensagem correspondente à classificação do IMC.
else: #Caso o IMC calculado seja maior ou igual a 40, indicando que a pessoa está com obesidade grau III.
    print("Você está com obesidade grau III.") #Exibe a mensagem correspondente à classificação do IMC.

# Perceba que o programa utiliza uma estrutura de decisão (if-elif-else) para classificar o IMC em diferentes categorias, de acordo com os valores estabelecidos pela OMS. Cada categoria possui uma faixa de valores específica, e o programa informa ao usuário em qual faixa ele se encontra com base no IMC calculado.
# Os valores de referência utilizados para a classificação do IMC são os seguintes:
# - Abaixo do peso: IMC < 18.5 
# - Peso normal: 18.5 ≤ IMC < 25
# - Sobrepeso: 25 ≤ IMC < 30
# - Obesidade grau I: 30 ≤ IMC < 35
# - Obesidade grau II: 35 ≤ IMC < 40
# - Obesidade grau III: IMC ≥ 40
# Perceba que utilizamos, por exemplo, 30 ≤ IMC < 35 para a classificação de obesidade grau I, o que significa que qualquer valor de IMC maior ou igual a 30 e menor que 35 será classificado como obesidade grau I. Da mesma forma, utilizamos 35 ≤ IMC < 40 para a classificação de obesidade grau II, e assim por diante. 
# Ou seja, cada faixa de valores é definida por um intervalo específico, e o programa verifica em qual intervalo o IMC calculado se encaixa para fornecer a classificação correta ao usuário.
# Se IMC for 34.99, o programa exibirá "Você está com obesidade grau I." Se IMC for 35.00, o programa exibirá "Você está com obesidade grau II." Se IMC for 39.99, o programa exibirá "Você está com obesidade grau II." Se IMC for 40.00, o programa exibirá "Você está com obesidade grau III."
# Não é necessário verificar explicitamente se o IMC é maior ou igual a 18.5, 25, 30 ou 35 nas condições elif, pois essas verificações já são implícitas devido à estrutura da lógica condicional. O programa termina aqui, tendo fornecido ao usuário o valor do IMC e a classificação correspondente de acordo com os padrões da OMS.
# O programa termina aqui, tendo fornecido ao usuário o valor do IMC e a classificação correspondente de acordo com os padrões da OMS.