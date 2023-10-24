#Apresentar todos os números divisíveis por 5 que sejam menores que 150.


for i in range(150):
    if (i %5 == 0):
        print("\n", i, "é divisível por 5 e é menor que 150.")


#Elaborar um programa que apresente no final, o somatório dos valores pares existentes na faixa de 10 até 20.
#OBS : começa em 10, termina em 21, e aumenta de 2 em 2.
total = int (0)
for cont in range(10, 21, 2):

    total = total + cont
print("\nO somatório dos valores pares existentes na faixa de 10 até 20 é", total, "\n")

#Elaborar um programa para imprimir os números de 1 (inclusive) a 10 (inclusive) em ordem decrescente.

for contador in range (10, 0, -1):
    print(contador)