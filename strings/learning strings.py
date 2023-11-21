nome = 'lucca'
nome_maiusculo = nome.capitalize()
print(nome_maiusculo)

nome2 = 'LUCCA'
nome_minusculo = nome.casefold()
print(nome_minusculo)

nome_maiusculo2 = nome.upper()
print(nome_maiusculo2)

print(nome2.isupper()) #verifica se a variável só tem letras maiúsculas
print(nome.islower()) #verifica se a variável só tem letras minúsculas

sobrenome = 'Duque'
nome_completo = nome.capitalize() + ' ' + sobrenome
print(nome_completo)

cpf = '11122233345'
print(cpf.isnumeric()) #verifica se a variável é totalmente numérica
print(cpf.isalpha()) #verifica se a variável é totalmente alfanumérica (apenas letras)
print(cpf.isalnum()) #verifica se tem letras ou números (por exemplo ,se tivessem --- no meio da str, daria falso)

for letra in nome: # printa todas as letras de uma variável, linha por linha.
    print(letra)
