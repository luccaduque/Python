#O comando for em Python é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string) 
#ou qualquer outro objeto iterável. Ele é frequentemente utilizado quando o número de iterações é conhecido.
#Por exemplo, o seguinte código em Python utiliza um loop for para imprimir os números de 0 a 4:

for i in range(5):
    print(i)


#Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 999 a 1500.

for num in range(999,1500):
        if num % 2 != 0:
              print(num)

#Apresentar o total da soma obtido de N números inteiros, a partir do número 1 até N.
#usar o + 1 foi necessário porque os numeros em python começam em 0!!

soma = 0
n = int (input("\nDigite um número inteiro ->  "))
for cont in range (n + 1):
    soma = soma + cont
print("O total da soma dos números de 1 até", n, "é", soma)

#Apresentar os resultados de uma tabuada de um número qualquer.
total = 0
numero = float (input("\nInsira um número qualquer ->  "))
for contador in range(11):
      total = contador * numero
      print("\n", contador, "x" , numero, "=", total)
