#Escreva uma função que recebe dois inteiros, m e n, como parâmetros e retorna a combinação m!/((m-n)!n!).
def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num-1)

#combinação   
def combinacao(m,n):
    resultado_fatorial_m = (fatorial(m))
    resultado_fatorial_n = (fatorial(n))
    m_menos_n_fatorial = fatorial(m-n)
    return resultado_fatorial_m/(m_menos_n_fatorial * resultado_fatorial_n)

m = int (input("\nInsira o valor de m ->  "))
n = int (input("\nInsira o valor de n ->  "))

resultado_combinacao = combinacao(m,n)
print(f"A combinação de {m} escolhidos {n} a {n} é: {resultado_combinacao}")
