def sumar(x, y):
    return x + y

def restar(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    try:
        return x / y
    except:
        print("No se puede divir por cero")
        
def imprimeMenu():
    print("Selecciona una opción")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def leerOpc():
    return input()

def leerValores():
    res = list()
    print("Dime un número:")
    num1 = int(input())
    res.append(num1)
    print("Dime otro número:")
    num2 = int(input())
    res.append(num2)
    return res