#Calcula média, se menor que 3.0 reprovado, se maior que 3.0 e menor que 6.0 IFA, se maior q 6.0 aprovado. 
#Quantos alunos foram aprovados reprovados ou ifa exiba no final. Use RESP e nome do aluno ! 

aprovado = int (0)
reprovado = int (0)
ifa = int (0)
resp = ''

resp = (input("\nVocê deseja iniciar o programa CALCULA MÉDIA? S para SIM  e n para NÃO ->  "))

while (resp == 's' or resp == 'S'):
    nome = input("\nInsira o nome do aluno ->  ")
    P1 = float (input("\nInsira a nota P1 ->  "))
    P2 = float (input("\nInsira a nota P2 ->  "))
    P3 = float (input("\nInsira a nota P3 ->  "))

    m = (P1 + P2 + P3) / 3

    if (m >= 6.0):
        print("\nO aluno", nome, "foi aprovado! Nota ->  ", m)
        aprovado = aprovado + 1

        elif (m > 3.1 and m < 6.0):
        print("\nO aluno", nome, "está de recuperação! Nota ->  ", m)
        ifa = ifa + 1

    elif (m < 3.0):
        print("\nO aluno", nome, "foi reprovado! Nota ->  ", m)
        reprovado = reprovado + 1

    resp = (input("Você deseja continuar? S para sim e N para não ->  "))
print("\n", aprovado, "aluno(s) foram aprovados.\n", ifa, "aluno(s) estão de recuperação.\n", reprovado, "aluno(s) foram reprovados!\n")
