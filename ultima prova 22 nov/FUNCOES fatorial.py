def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)

numero = int (input ("\nInsira o numero desejado ->  "))
if (numero < 0):
    print("\nNão existe fatorial de numero negativo.")
else:
    resultado = fatorial(numero)
    print(resultado)