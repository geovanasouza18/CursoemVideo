x = 0
while x < 10:
    if x == 5:
        print("Achei a pista! 🔍")
    x += 1

#CASO 1 — O Contador da Torre do Relógio
contador = 0
while contador < 5:
    print(contador)
    contador += 1

#CASO 2 — A Porta Só Abre Com a Palavra Secreta
senha = input('Digite a senha para acessar: ')
while senha != 'london':
        senha = input('Senha incorreta! Tente novamente: ')
print('Acesso permitido!')

#CASO 3 — O Robô Sentinela Noturno
while True:
    nome = input('Digite a palavra para parar o robô: ')
    if nome == 'shutdown':
        break

#CASO 4 — A Batalha das Variáveis
energia = 10
fome = 0
while energia > 0 and fome < 5:
    print(energia)
    energia -= 1
    fome += 1