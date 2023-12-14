from math import sqrt
def fibonacci_linear():
    #Utilizando  a Fórmula de Binet
    n = int(input())

    if n >= 0:
        termo = (((1 + sqrt(5))**n) - ((1 - sqrt(5)))**n) / (2**n * sqrt(5))
        print(round(termo))
    else:
        print("Não é possível utilizar este número")

fibonacci_linear()