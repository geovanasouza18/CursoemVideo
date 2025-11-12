from random import randint
import time
computador = randint(0, 5) #faz o computador pensar
tentativa = 0

print("Vou pensar em um número entre 0 e 10, Tente adivinhar...")
time.sleep(1)
jogador = int(input("Em que número eu pensei? "))

while computador != jogador:
    jogador = int(input('Você errou! Tente novamente! '))
    tentativa += 1
print(f'Você venceu! Mas teve que tentar {tentativa} vezes.')