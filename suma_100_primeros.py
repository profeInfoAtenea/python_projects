import time
N = 100
'''
Sumar los N primeros números
'''

'''
# RECURSIVAMENTE
'''
def suma_rec(n):
    if(n==0):
        return 0
    else:
        return n + suma_rec(n-1)

inicio = time.time()
print("suma es: ",suma_rec(N))
fin = time.time()
total = fin - inicio
print("Tiempo total: ", total)

'''
# USANDO FOR
'''
def bucle_for(n):
    suma = 0
    for i in range(1, n+1):
        suma = i + suma
    return suma
inicio = time.time()
print("suma es: ", bucle_for(N))
fin = time.time()
total = fin - inicio
print("Tiempo total: ", total)

'''
# USANDO WHILE
'''
def bucle_while(n):
    suma = 0
    index = 1
    while(index <= n):
        suma = index + suma
        index += 1
    return suma    
inicio = time.time()
print("suma es: ", bucle_while(N))
fin = time.time()
total = fin - inicio
print("Tiempo total: ", total)
