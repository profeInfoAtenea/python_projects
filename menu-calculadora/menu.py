from aritmetica import *

interruptor = True

while(interruptor):
    imprimeMenu()
    opc = leerOpc()
    if(opc == '1'):
        val = leerValores()
        print("El resultado de sumar es ", sumar(val[0], val[1]))
    elif(opc == '5'):
        interruptor = False