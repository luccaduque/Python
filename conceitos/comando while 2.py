#Entrar com números enquanto forem positivos. Quando entrar com número 0
#ou algum número negativo, imprimir quantos números foram digitados.


qtd = int (0)
n = float (1)
while (n > 0):
    n = float (input("\nInsira um número qualquer ->  "))
    qtd = qtd + 1
print("\nForam digitados", qtd, "números.")

