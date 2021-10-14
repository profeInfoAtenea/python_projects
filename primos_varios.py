'''Escriba un algoritmo que proporcione
los números primos comprendidosentre 1 y 1000.
Recuerde que un número primo solo es divisible
entre sí mismo y por la unidad.
Preste atención, lo más sencillo
no siempre es lo más rápido'''

#DAVID 
print("1")
CANTIDAD = 1000
for i in range(2, CANTIDAD):
    primo = 1
    for x in range(2, i-1):
        if(i%x == 0):
            primo = 0
            break
    if(primo == 1):
        print(i)
        
#ADRIAN
x = 0
n = 2
divisores = 0

while(x < 1000):
    x = x + 1
    n = 2
    divisores = 0
    if(x < 2):
        print(x)
    else:
        while(n < 1000):
            if(x % n == 0):
                divisores += 1
            n = n + 1
    if(divisores == 1):
        print(x)
        
#uso de funciones - código limpio
def es_primo(n):
    for i in range(2, n//2):
        if(n % i == 0):
            return False
    return True
        
lista = []

for i in range(1, 1000):
    if(es_primo(i)):
       lista.append(i)

for i in lista:
    print(i)

