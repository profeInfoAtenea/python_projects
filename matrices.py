import random
import numpy as np

''' Genera una lista de 15 elementos aleatorios entre 1 y 10 '''
def genera_lista():
    lst = [random.randint(0, 10) for x in range(15)]
    return lst


'''a) Con valores aleatorios entre 1 y 10,
y a continuación diga cuantos pares e impares hay.'''

def apartado_a(lista):
    pares = 0
    impares = 0
   
    for i in lista:
        if(i % 2 == 0):
            pares+=1
        else:
            impares+=1
    ret = [pares, impares]
    return ret
    
lst = genera_lista()
print("Pares: ", apartado_a(lst)[0])
print("Impares: ", apartado_a(lst)[1])

'''
### Genera Matrices Aleatorias de Vectores a partir de ( filas y columnas )
'''
def generaMatricesRandom(filas, columnas):
    matriz = [[random.randint(0, 10)  for x in range(filas)] for i in range(columnas)]
    return matriz


    

#print( generaMatricesRandom(3,3))

''''

Se llama matriz identidad
de orden n
y
se nota en una matriz cuadrada
de orden n

en la que los elementos de la diagonal principal
son 1 y el resto 0.

identidad_3 = [[1,0,0],[0,1,0],[0,0,1]]

'''
identidad_3 = [[1,0,0],[0,1,0],[0,0,1]]

def multiplicaMatrices(matriz1, matriz2):
    print("3 x 3 Random")
    print("Matriz A:")
    print(matriz1)
    print("Matriz B:")
    print(matriz2)
    matrizsuma = sumarMatrices(matriz1,matriz2);
    print("Matriz matrizSuma:")
    print(matrizsuma)


def sumarMatrices(matriz1, matriz2):
    return [[matriz1[0][0] + matriz2[0][0] , matriz1[0][1] + matriz2[0][1] , matriz1[0][2] + matriz2[0][2]],[matriz1[0][0] + matriz2[0][0] , matriz1[0][1] + matriz2[0][1] , matriz1[0][2] + matriz2[0][2]],[matriz1[0][0] + matriz2[0][0] , matriz1[0][1] + matriz2[0][1] , matriz1[0][2] + matriz2[0][2]]]

def negativaMatriz(matriz):
    return [[matriz[0][0]*-1,matriz[0][1]*-1,matriz[0][2]*-1],[matriz[1][0]*-1,matriz[1][1]*-1,matriz[1][2]*-1],[matriz[2][0]*-1,matriz[2][1]*-1,matriz[2][2]*-1] ]

def transpuestaMatriz(matriz):
    x=np.array(matriz)
    return np.transpose(x)
     
    
    
a = generaMatricesRandom(3,3)
print("print A")
print(a)
print("print B")
b = generaMatricesRandom(3,3)
print(b)
print("print A + B")
print(sumarMatrices(a,b))
print("print -A")
print(negativaMatriz(a))
print("print A-A")
print(sumarMatrices(a, negativaMatriz(a)))

print("print  traspuesta A ")
a_t = transpuestaMatriz(a)
print(a_t)


a_np = np.array(a)
a_inv = np.linalg.inv(a)
b_np= np.array(b)

print("A =", a_np)

print("b =", b_np)

print("Ab =",np.matmul(a,b))
print("a inv a =",np.matmul(a,a_inv))

np.zeros_like(a) # Matriz de ceros con la forma de a
np.ones_like(a) # Matriz de unos con la forma de a
np.identity(3)

en la que los elementos de la diagonal principal
son 1 y el resto 0.

identidad_3 = [[1,0,0],[0,1,0],[0,0,1]]

'''
identidad_3 = [[1,0,0],[0,1,0],[0,0,1]]

def multiplicaMatrices(matriz1, matriz2):
    print("3 x 3 Random")
    print("Matriz A:")
    print(matriz1)
    print("Matriz B:")
    print(matriz2)
    matrizsuma = sumarMatrices(matriz1,matriz2);
    print("Matriz matrizSuma:")
    print(matrizsuma)


def sumarMatrices(matriz1, matriz2):
    return [[matriz1[0][0] + matriz2[0][0] , matriz1[0][1] + matriz2[0][1] , matriz1[0][2] + matriz2[0][2]],[matriz1[0][0] + matriz2[0][0] , matriz1[0][1] + matriz2[0][1] , matriz1[0][2] + matriz2[0][2]],[matriz1[0][0] + matriz2[0][0] , matriz1[0][1] + matriz2[0][1] , matriz1[0][2] + matriz2[0][2]]]

def negativaMatriz(matriz):
    return [[matriz[0][0]*-1,matriz[0][1]*-1,matriz[0][2]*-1],[matriz[1][0]*-1,matriz[1][1]*-1,matriz[1][2]*-1],[matriz[2][0]*-1,matriz[2][1]*-1,matriz[2][2]*-1] ]

def inversaMatriz(matriz):
    return [[1/(matriz[0][0]),1/(matriz[0][1]),1/(matriz[0][2])],[1/(matriz[1][0]),1/(matriz[1][1]),1/(matriz[1][2])],[1/(matriz[2][0]),1/(matriz[2][1]),1/(matriz[2][2])] ]

def transpuestaMatriz(matriz):
    x=np.array(matriz)
    return np.transpose(x)
     
    
    
a = generaMatricesRandom(3,3)
print("print A")
print(a)
print("print B")
b = generaMatricesRandom(3,3)
print(b)
print("print A + B")
print(sumarMatrices(a,b))
print("print -A")
print(negativaMatriz(a))
print("print A-A")
print(sumarMatrices(a, negativaMatriz(a)))
print("print  A")
print(inversaMatriz(a))
