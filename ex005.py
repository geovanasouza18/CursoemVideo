import time
#Caso 1 — O Cofre que Só Abre com Contagem
contador = 0
while contador < 10:
    print(contador)
    contador += 1
print('Cofre aberto 🔓')

#Caso 2 — O Suspeito das Tentativas Infinitas
senha = input('Insira sua senha: ')
while senha != '1234':
    senha = input('Senha incorreta! Digite novamente: ')
print('Acesso concedido')

#Caso 3 — A Fuga do Número Fantasma
contador2 = 50
while contador2 > 0:
    print(contador2)
    contador2 -= 5
print('Sumiu na neblina')

#Caso 4 — O Interrogatório dos Ímpares
impar = 0
while impar < 20:
    if impar % 2 != 0:
        print(f'{impar} Suspeito encontrado 🔎')
    impar += 1

#Caso 5 — A Bomba Relógio Matemática
bomba = int(input('Insira um numero: '))
while bomba > 0:
    print(bomba)
    time.sleep(1)
    bomba -= 1
print('Bomba desativada por Sherlock Holmes')

#Caso 6 — O Cofre que Só Abre com Números Pares
par = 2
while par <= 30:
    if par % 2 == 0:
        print(f'{par} Número aceito 🔐')
    par += 1

#Caso 7 — O Viciado no Loop Infinito
palavra_secreta = 'sair'
while True:
    palavra = input('Insira uma palavra: ')
    if palavra == palavra_secreta:
        break
print('Operação encerrada 🗝️')