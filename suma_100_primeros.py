import time

def suma_rec(x, total):
    if(x == 1):
        return 1
    else:
        total = suma_rec(x-1, total) + x
    return total
inicio = time.time()
print("suma es: ",suma_rec(100,0))
fin = time.time()
total = fin - inicio
print("Tiempo total: ", total)

def bucle_for():
    suma = 0
    for i in range(1, 101):
        suma = i + suma
    return suma
inicio = time.time()
print("suma es: ", bucle_for())
fin = time.time()
total = fin - inicio
print("Tiempo total: ", total)
def bucle_while():
    suma = 0
    index = 1
    while(index <= 100):
        suma = index + suma
        index += 1
    return suma    
inicio = time.time()
print("suma es: ", bucle_while())
fin = time.time()
total = fin - inicio
print("Tiempo total: ", total)
