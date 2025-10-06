"""import time
print("Vou pensar em um número entre 0 e 5, Tente adivinhar...")
num = int(input("Em que número eu pensei?"))
print("Procesando...")
time.sleep(1)
if num == 3:
    print("Você venceu!")
else:
    print("Você perdeu!")
"""
from random import randint
import time
computador = randint(0, 5) #faz o computador pensar
print("Vou pensar em um número entre 0 e 5, Tente adivinhar...")
jogador = int(input("Em que número eu pensei? "))
print("Procesando...")
time.sleep(1)
if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(computador, jogador))