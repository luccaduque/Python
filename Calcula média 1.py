#Calcula média, se menor que 3.0 reprovado, se maior que 3.0 e menor que 6.0 IFA, se maior q 6.0 aprovado. Quantos alunos foram aprovados reprovados ou ifa exiba no final.

aprovado = int (0)
reprovado = int (0)
ifa = int (0)
i = int (0)

while (i < 3): #numero de exemplo!!
    print("\n")
    P1 = float (input("\nDigite a nota 1 ->  "))
    P2 = float (input("\nDigite a nota 2 ->  "))
    P3 = float (input("\nDigite a nota 3 ->  "))

    m = (P1 + P2 + P3) / 3


    if (m >= 6.0):
        print("\nVocê foi aprovado! Sua nota eh ", m, "\n")
        aprovado = aprovado + 1  

    elif (m > 3.1 and m < 6.0):
        print("\nVocê está de recuperação! Sua nota eh ", m, "\n")
        ifa = ifa + 1

    elif (m <= 3.0):
        print("\nVocê está reprovado! Sua nota eh ", m, "\n")
        reprovado = reprovado + 1
    i = i + 1

print(aprovado, "aluno(s) foram aprovados.\n")
print(ifa, "aluno(s) ficaram de recuperação.\n")
print(reprovado, "aluno(s) foram reprovados.\n")