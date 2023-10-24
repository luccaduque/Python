#Faça um programa que leia 10 números inteiros, ao final, exiba a quantidade de números ímpares e pares que foram inseridos.
#Também exiba o MAIOR par e o MENOR ímpar.
qtdPAR = 0
qtdIMPAR = 0
maiorPAR = 0
menorIMPAR = 0
for i in range(0, 10):
    n = int(input("\nDigite um número INTEIRO ->  "))
    if (n % 2 == 0):
        qtdPAR = qtdPAR + 1
        if (n > maiorPAR):
            maiorPAR = n
    if (n % 2 != 0):
        qtdIMPAR = qtdIMPAR + 1
        if (menorIMPAR == 0 or n < menorIMPAR):
            menorIMPAR = n
if (menorIMPAR == 0):
    print("\nO maior número par é", maiorPAR, ". Não foram inseridos números impares. Foram inseridos", qtdPAR, "números pares.")
if (maiorPAR == 0):
    print("\nO menor ímpar é", menorIMPAR, ". Não foram inseridos números pares. Foram inseridos", qtdIMPAR, "números ímpares.")
if (menorIMPAR >= 1 and maiorPAR >=1):
    print("\nO maior número par é", maiorPAR, "e o menor ímpar é", menorIMPAR, ". Foram inseridos", qtdIMPAR, "números ímpares e", qtdPAR, "números pares.")
