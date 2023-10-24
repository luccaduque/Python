#Entrar com 15 números e apresente a soma e a média desses números.
soma = float(0)
for cont in range(0,15):
    n = float (input("\nDigite um número qualquer ->  "))
    soma = soma + n
media = soma / 15
print("\nA soma dos números inseridos é ", soma, "e a média é ", media)