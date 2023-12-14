def fibonacci_recursivo():
    n = int(input())
    ultimo = 1 
    penultimo = 1

    if n >= 0:
        if n == 0:
            print(0)
        elif n == 1 or n == 2:
            print("1")
        else:
            count = 3
            while count <= n:
                termo = ultimo + penultimo
                penultimo = ultimo
                ultimo = termo
                count += 1
            print(termo)
    else:
        print("Não é possível utilizar este número")
        
fibonacci_recursivo()