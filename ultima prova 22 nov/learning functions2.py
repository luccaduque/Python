#Crie uma função que faça o tratamento do textos dos produtos, deixe todos com letra MAIUSCULA e sem espeçaos vazios.
produtos = 'aB235ut5', ' aB5423', 'abc21342351235        ', 'bCfgHWERT45'

def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto

produtos_tratados = []

for produto in produtos:
    produto_tratado = tratar_texto(produto)
    produtos_tratados.append(produto_tratado)
print(produtos_tratados)