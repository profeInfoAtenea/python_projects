import time

def factorial_while(n):
    ret = n
    while(n>1):
        n-=1
        ret = ret * n
    return ret

def factorial_for(n):
    ret = n
    for i in range(1, n):
        ret = ret * i
    return ret

def factorial_rec(n):
    if(n == 1):
        return 1
    else:
        return n * factorial_rec(n-1)
#

#
N = 1416
'''
# El valor obtenido se corresponde con los segundos
# que han transcurrido desde el comienzo de la época:
'''
# 1 de enero de 1970, 0 hora
print("Han trascurrido ", time.time(), " segundos desde el 1 de enero de 1970 #Función: Time.Time()")
'''
#
'''
print("Cálculo de factorial(",N,") ")
n = N
inicio = time.time()
res_fact_while = factorial_while(n)
fin = time.time()
total = fin - inicio
print("Tiempo factorial_while: ",total)

inicio = time.time()
res_fact_for = factorial_for(n)
fin = time.time()
total = fin - inicio
print("Tiempo factorial_for: ",total)

inicio = time.time()
res_fact_rec = factorial_rec(n)
fin = time.time()
total = fin - inicio
print("Tiempo factorial_rec: ",total)


print("res_fact_while:",res_fact_while,", res_fact_for:",res_fact_for, "res_fact_rec:",res_fact_rec)
