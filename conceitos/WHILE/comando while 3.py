#Ler vários números e informar quantos números entre 100 e 200 foram
#digitados. Quando o valor 0 for informado o programa deverá encerrar.

n = float
qtd = int (0)
while (n != 0):
    n = float (input("\nInsira um número qualquer ->  "))
    if (n >= 100 and n <= 200):
        qtd = qtd + 1
print("\nForam digitados", qtd, "números entre 100 e 200.")