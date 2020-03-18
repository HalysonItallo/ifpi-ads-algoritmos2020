import math

def main():
    cof_A = float(input("Digite o coeficiente 'A': "))
    cof_B = float(input("Digite o coeficiente 'B': "))
    cof_C = float(input("Digite o coeficiente 'C': "))

    print(raiz_cof(cof_A, cof_B, cof_C))
    
    
def raiz_cof(A, B, C):
    if A != 0:
        delta = float(math.sqrt(B**2 - 4*A*C))
        x1 = ((-1*B) + delta) / (2*A)
        x2 = ((-1*B) - delta) / (2*A)
        return "A raiz 1: %.2f a raiz 2: %.2f"%(x1,x2)
    else:
        return "'A' não pode ser 0"


main()