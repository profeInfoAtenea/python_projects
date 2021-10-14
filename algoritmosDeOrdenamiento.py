# Recursos de : 
# - https://eiposgrados.com/blog-python/tipos-de-algoritmos-de-ordenacion-en-python/
# - https://www.geeksforgeeks.org/merge-sort/
# 'Aprender Inteligencia Artificial, Combinatoria, Grafos y Algoritmos en Python con 100 ejercicios prácticos, Arnaldo Pérez Castaño'

import time
LISTADO = [32423,312,1,3,43213,2,5,1,5,9,8,2,1,231,3,-3,5,1,43,1,6,123,-6,32423,312,1,3,43213,2,5,1,5,9,8,2,1,231,3,-3,5,1,43,1,6,123,-6,32423,312,1,3,43213,2,5,1,5,9,8,2,1,231,3,-3,5,1,43,1,6,123,-6]
'''
Ordenamiento de burbuja (Bubble Sort)

Este algoritmo de clasificación simple itera sobre la lista de datos, 
comparando elementos en pares hasta que los elementos más grandes “burbujean” 
hasta el final de la lista y los más pequeños permanecen al principio.

Comienza comparando los dos primeros elementos de la lista, si el primer elemento 
es mayor que el segundo, los intercambiamos, si no, se quedan como están.
Luego pasamos al siguiente par de elementos, los comparamos e intercambiamos 
si fuera necesario. 
'''

def bubbleSort(list_nums):
    #Establecemos la variable de intercambio en True para entrar en el bucle al menos una vez
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(list_nums) - 1):
            if list_nums[i] > list_nums[i+1]:
                #Intercambiamos los datos
                list_nums[i], list_nums[i+1] = list_nums[i+1], list_nums[i]
                # Cambiamos a True la variable ya que ha habido un intercambio
                intercambio = True
   

'''
Orden de selección (Selectión Sort)

Este algoritmo separa la lista en dos partes, ordenada y no ordenada. Continuamente “elimina” el elemento más pequeño
de la parte sin ordenar y lo agrega a la parte ordenada.

Lo que realmente realiza este algoritmo es tratar la parte izquierda de la lista como la parte ordenada buscando en toda
la lista el elemento más pequeño y poniéndolo el primero. Después, sabiendo que ya tenemos el elemento más pequeño el primero,
buscamos en toda la lista el elemento más pequeño de los restantes sin ordenar y lo intercambiamos con el siguiente ordenado y
así hasta acabar con la lista.

Cuantos más elementos tengamos ordenados, menos elementos tendremos que examinar.
'''
def selectionSort(list_nums):
    #El valor de i corresponde al número de datos que se ordenaron
    for i in range(len(list_nums)):
        #Entendemos que el primer elemento sin ordenar es el más peuqeño
        lowest_value_index = i
        #Este bucle trabaja sobre los elementos no clasificados
        for j in range(i+1, len(list_nums)):
            if list_nums[j] < list_nums[lowest_value_index]:
                lowest_value_index = j
        #Intercambia el valor del elemento sin ordenar más bajo
        # con el primero sin ordenar
        list_nums[i], list_nums[lowest_value_index] = list_nums[lowest_value_index], list_nums[i]

'''
Tipo de inserción (Insert Sort)

Este algoritmo, al igual que la clasificación por selección, separa la lista en dos partes, ordenadas y no ordenadas.
También suponemos que el primer elemento está ordenado, luego pasamos al siguiente elemento que lo vamos a llamar X, 
comparamos X con el primero, si es mayor, se queda como está pero si es más pequeño, copiamos el primer elemento en la segunda
posición e insertamos X como primero.
'''

def insertionSort(list_nums):
    #Entedemos que el primer elemento sin ordenar es el más peuqeño
    # así que comenzamos con el segundo
    for i in range(1, len(list_nums)):
        item_to_insert = list_nums[i]
        #Guardamos en j el índice del elemto anterior
        j = i - 1
        #Movemos todos los elementos de la lista hacia adelante si son
        #mayores que el elemento a insertar
        while j >= 0 and list_nums[j] > item_to_insert:
            list_nums[j+1] = list_nums[j]
            j -= 1
        # Insertamos el elemento
        list_nums[j+1] = item_to_insert

'''
 Combinar ordenación (Merge Sort)
 
 Este algoritmo comienza dividiendo la lista en dos, luego esas dos mitades en 4 y así sucesivamente hasta que 
 tengamos listas de un elemento de longitud. Después, estos elementos se vuelven a unir en orden. Primero fusionaremos 
 los elementos individuales en pares de nuevo ordenándolos entre sí, luego seguiremos ordenándolos en grupos hasta que 
 tengamos una sola lista ordenada.
 '''
def mergeSort(list_nums):
    if len(list_nums) > 1:
  
         # Finding the mid of the array
        mid = len(list_nums)//2
  
        # Dividing the array elements
        L = list_nums[:mid]
  
        # into 2 halves
        R = list_nums[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list_nums[k] = L[i]
                i += 1
            else:
                list_nums[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            list_nums[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            list_nums[k] = R[j]
            j += 1
            k += 1
  
# To heapify subtree rooted at index i.
# n is size of heap
 
 
def heapify(list_nums, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and list_nums[largest] < list_nums[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and list_nums[largest] < list_nums[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        list_nums[i], list_nums[largest] = list_nums[largest], list_nums[i]  # swap
 
        # Heapify the root.
        heapify(list_nums, n, largest)
 
# The main function to sort an array of given siz

def heapSort(list_nums):
    n = len(list_nums)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(list_nums, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        list_nums[i], list_nums[0] = list_nums[0], list_nums[i]  # swap
        heapify(list_nums, i, 0)


'''
QuickSort

El Ordenamiento Rápido(QuickSort en inglés) es un eficiente método que se emplea y estudia con frecuencia
a pesar de tener más de 50 años de antigüedad.

1.- Es un algoritmo basado en comparaciones y como todo algoritmo de este tipo, su complejidad temporal no puede bajar de O(nlgn)
2.- Emplea la conocida técnica de Divide y Venceras para dividir el problema (ordenación) en subproblemas y resolverlos (ordenarlos), simplificando así el proceso de resolución final
3.- La estrategia en general es la siguiente:
      a. Divide: Realizar la partición de la lista A[i..j] en dos sublistas A[i..k-1] y A[k+1..j], de modo que todo elmento en la primera sea menor o igual que A[k] y todo elemento en la segunda sea mayor que este valor
      A[k] es nombrado elemento pivote y rige el orden de la lista en un nivel de la recursividad. Existen diferentes técnicaas para escotger el elmento pivote, en este caso escogeremos siempre el último elemento de la lista.
      
      b. Conquista: Ordenar sublistas A[i..k-1] y A[k+1..j] realizando llamados recursivos al algoritmo QuickSort
      
      c. Combina: Dado que las sublistas están ordenadas y todo elemento de la primera es menor que cada elemento de la segunda, la lista completa se encuentra ordenada y el procedimiento ha concluido
4.- Las operaciones del procedimiento se realizan en el siguiente orden
    a. Escoger un elmento pivote A[k] (en nuestro caso siempre el último)
    b. Reubicar los elementos de manera que los menors o iguales a A[k] se encuentran a su izquierda en la lista y los mayors, a su derecha
    c. Continuar recursivamente el procedimiento en cada una de las sublistas anteriores.
       La primera está conformada por los valores menores o iguales a A[k] y la segunda por los valores mayores. La recursividad se detiene cuando la longitud de una sublista es menor que 2.
    d. Una pieza clave es el algoritmo es el método pariticiona, que reorganiza la lista en dos partes: aquella con elementos menores o iguales que x (a su izquierda) y aquella con elementos mayores ( a su derecha).
       Este método mantiene siempre un índice k que va incrementando y marca la división antes descrita.
      

'''
def quickSort(list_nums):
    def quicksortRec(list_nums, i, j):
        if i < j:
            k = particion(list_nums, i, j)
            quicksortRec(list_nums, i, k-1)
            quicksortRec(list_nums, k+1, j)
    quicksortRec(list_nums, 0, len(list_nums)-1)

def particion(list_nums, i, j):
    x = list_nums[j]
    k = i - 1
    for h in range(i, j):
        if list_nums[h] <= x:
            k += 1
            temp = list_nums[h]
            list_nums[h] = list_nums[k]
            list_nums[k] = temp
    temp= list_nums[k+1]
    list_nums[k+1] = list_nums[j]
    list_nums[j] = temp
    return k + 1
  
  
'''
    #############################################
    #                TESTING  TIME              #
    #############################################
'''
  
  
  
# Comprobamos el funcionamiento
''' bubbleSort '''
listaNumeroAleatorios = LISTADO
print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
bubbleSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total bubbleSort: ", total)


''' selectionSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
selectionSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total selectionSort: ", total)

''' insertionSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
insertionSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total insertionSort: ", total)


''' mergeSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
mergeSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total mergeSort: ", total)

''' insertionSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
insertionSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total insertionSort: ", total)

''' mergeSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
insertionSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total mergeSort: ", total)

''' heapSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
insertionSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total heapSort: ", total)


''' quickSort '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
quickSort(listaNumeroAleatorios)
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total quickSort: ", total)


''' sort de list '''
listaNumeroAleatorios = LISTADO
#print("lista desordenada:", listaNumeroAleatorios)
inicio = time.time()
listaNumeroAleatorios.sort()
fin = time.time()
total = fin - inicio
#print("lista ordenada:", listaNumeroAleatorios)
print("Tiempo total sort de list: ", total)
