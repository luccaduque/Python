#comando while  
#while (condição):
#    instruções

#Entrar com números e imprimir o triplo de cada número. O programa encerra quando o usuário informar o número -999.
n = int (0)
triplo = 0
while (n != -999):
    n = int (input ("Insira um número qualquer ->  "))
    if (n != -999):
        triplo = 3 * n
        print("\nO triplo de", n, "é", triplo, "\n")
    
