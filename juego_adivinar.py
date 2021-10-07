import random
intentos = 3
num_secreto = random.randint(1, 10)
''' para testing
print(num_secreto)
'''
print("Adivina un número entre 1 y 100")
num = int(input())

while((num_secreto != num) and (intentos > 1)):
    if(num_secreto > num):
        print("Es muy bajo")
    else:
        print("Es muy alto")
    intentos -= 1
    print("Intentalo de nuevo, te quedan ", intentos, " intentos")
    num = int(input())
    
if(num_secreto == num):
    quedan = 4 - intentos
    print("Bien!, has adivinado en ", quedan, " intentos")
else:
    print("Lo siento. El número era ", num_secreto) 
