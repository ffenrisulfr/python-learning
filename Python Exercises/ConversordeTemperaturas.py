Pergunta = input("Digite a temperatura que você deseja converter (Celsius - C | Fahrenheit - F | Kelvin - K): ").upper()

ObterResposta = Pergunta

if(ObterResposta == "C"): C = float(input("digite em C: "))
if(ObterResposta == "F"): F = float(input("digite em F: "))
if(ObterResposta == "K"): K = float(input("digite em K: "))

Pergunta2 = input("Para qual medida você deseja saber? (Celsius - C | Fahrenheit - F | Kelvin - K): ").upper()

if(Pergunta == "F" and Pergunta2 == "C"):
    conversorFparaC= (F - 32)/1.8
    print("O valor", F, "em °Fahrenheit é equivalente a", conversorFparaC, "em °Celsius")
elif(Pergunta == "C" and Pergunta2 == "F"):
    conversorCparaF= (C * 1.8 + 32)
    print("O valor", C, "em °Celsius é equivalente a", conversorCparaF, "em °Fahrenheit")
elif(Pergunta == "K" and Pergunta2 == "C"):
    conversorKparaC= K - 273
    print("O valor", K, "em Kelvin é equivalente a", conversorKparaC, "em °Celsius")
elif(Pergunta == "C" and Pergunta2 == "K"):
    conversorCparaK= C + 273
    print("O valor", C, "em °Celsius é equivalente a", conversorCparaK, "em Kelvin")
elif(Pergunta == "F" and Pergunta2 == "K"):
    conversorFparaK= ((F - 32)/1.8) + 273
    print("O valor", F, "em °Fahrenheit é equivalente a", conversorFparaK, "em Kelvin")
elif(Pergunta == "K" and Pergunta2 == "F"):
    conversorKparaF= (K - 273)*1.8 + 32
    print("O valor", K, "em Kelvin é equivalente a", conversorKparaF, "em °Fahrenheit")