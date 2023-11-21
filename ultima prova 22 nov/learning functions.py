#comando 'def' define uma função
def soma (x,y):
    return x + y #devolva x + y

print(soma(10,20))
print(soma(-20,100))

def multiplicacao (x,y):
    return x * y
print(multiplicacao(10,5))
print(multiplicacao(-5,65))

#exemplos mais complexos
result_complexo = multiplicacao(soma(20,30), multiplicacao(1,2))
print(result_complexo)

#Observe que as variáveis 'x,y,z' da função soma não são os mesmos das outras funções.

def nome_do_seu_time ():
    return "VASCO DA GAMA"
print(nome_do_seu_time())