#EQUAÇÃO 2 GRAU BHASKARA
# delta = b^2 - 4.a.c
# x = -b +- raiz de delta / 2*a
import math
xis1 = int
xis2 = int

def delta (a, b, c):
    return b**2 - 4 * a * c
a = int (input("Insira o valor de a ->  "))
b = int (input("\nInsira o valor de b ->  "))
c = int (input("\nInsira o valor de c ->  "))
resultado_delta = int (delta (a,b,c))
print("\nO resultado do delta é ->  ", resultado_delta)

if resultado_delta == 0:
    xis1 = (-b + math.sqrt(resultado_delta)) / (2*a)
    print("\nx1 = ", xis1)
elif resultado_delta > 0:
    xis1 = (-b + math.sqrt(resultado_delta)) / (2*a)
    xis2 = (-b - math.sqrt(resultado_delta)) / (2*a)
    print("\nx1 = ", xis1,"\nx2 = ",xis2)
elif resultado_delta < 0:
    print("\nNão existem raízes de números negativos.")
