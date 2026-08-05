# Solicita ao usuário qual unidade de temperatura ele deseja converter.
# O método upper() transforma a resposta em letra maiúscula para facilitar a comparação.

Pergunta = input("Digite a temperatura que você deseja converter (Celsius - C | Fahrenheit - F | Kelvin - K): ").upper()

# Armazena a unidade escolhida pelo usuário para ser utilizada nas condições abaixo.
ObterResposta = Pergunta

# Verifica qual foi a unidade escolhida e solicita o valor da temperatura correspondente.
if(ObterResposta == "C"): C = float(input("digite em C: "))
if(ObterResposta == "F"): F = float(input("digite em F: "))
if(ObterResposta == "K"): K = float(input("digite em K: "))

# Solicita ao usuário para qual unidade ele deseja converter a temperatura.
Pergunta2 = input("Para qual medida você deseja saber? (Celsius - C | Fahrenheit - F | Kelvin - K): ").upper()

# Verifica a unidade inicial e a unidade desejada para realizar a conversão correta.

# Conversão de Fahrenheit para Celsius:
# Fórmula: C = (F - 32) / 1.8
if(Pergunta == "F" and Pergunta2 == "C"):
    conversorFparaC= (F - 32)/1.8
    print("O valor", F, "em °Fahrenheit é equivalente a", conversorFparaC, "em °Celsius")

# Conversão de Celsius para Fahrenheit:
# Fórmula: F = (C * 1.8) + 32
elif(Pergunta == "C" and Pergunta2 == "F"):
    conversorCparaF= (C * 1.8 + 32)
    print("O valor", C, "em °Celsius é equivalente a", conversorCparaF, "em °Fahrenheit")

# Conversão de Kelvin para Celsius:
# Fórmula: C = K - 273
elif(Pergunta == "K" and Pergunta2 == "C"):
    conversorKparaC= K - 273
    print("O valor", K, "em Kelvin é equivalente a", conversorKparaC, "em °Celsius")

# Conversão de Celsius para Kelvin:
# Fórmula: K = C + 273
elif(Pergunta == "C" and Pergunta2 == "K"):
    conversorCparaK= C + 273
    print("O valor", C, "em °Celsius é equivalente a", conversorCparaK, "em Kelvin")

# Conversão de Fahrenheit para Kelvin:
# Primeiro converte Fahrenheit para Celsius e depois Celsius para Kelvin.
elif(Pergunta == "F" and Pergunta2 == "K"):
    conversorFparaK= ((F - 32)/1.8) + 273
    print("O valor", F, "em °Fahrenheit é equivalente a", conversorFparaK, "em Kelvin")

# Conversão de Kelvin para Fahrenheit:
# Primeiro converte Kelvin para Celsius e depois Celsius para Fahrenheit.
elif(Pergunta == "K" and Pergunta2 == "F"):
    conversorKparaF= (K - 273)*1.8 + 32
    print("O valor", K, "em Kelvin é equivalente a", conversorKparaF, "em °Fahrenheit")