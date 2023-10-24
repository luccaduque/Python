#Pedir o nome e sexo de uma pessoa. Apresentar no final quantas pessoas são
#do sexo masculino e quantas são do sexo feminino. O programa encerra
#quando o usuário digitar FIM no nome da pessoa.

qtdF = int (0)
qtdM = int (0)
qtdX = int (0)
sexo = ''
nome = ''
while (nome != "FIM" or nome == "fim"):
    nome = input("\nQual é o seu nome? (Digite FIM para encerrar) ->  ")
    if (nome == 'FIM' or nome == 'fim'):
        break
    sexo = input("\nQual é o seu sexo? M para masculino, F para feminino e X para não-binário ->  ")
    if (sexo == 'm' or sexo == 'M'):
        qtdM = qtdM + 1
    if (sexo == 'f' or sexo == 'F'):
        qtdF = qtdF + 1
    if (sexo == 'x' or sexo == 'X'):
        qtdX = qtdX + 1
print("\nPessoas de sexo feminino:  ", qtdF, "\nPessoas de sexo masculino:  ", qtdM,"\nPessoas não-binárias:  ", qtdX)
