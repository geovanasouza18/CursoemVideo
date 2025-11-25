from random import randint

print('\033[33m===== Vamos jogar par ou ímpar =====\033[0m')
vitorias = 0
while True:
    computador = randint(0, 10)
    num = int(input('Diga um valor: '))
    opcao = str(input('Par ou ímpar? [P/I] ')).strip().upper()

    soma = num + computador
    resultado_par = soma % 2 == 0

    print(f'Você jogou {num} e o computador {computador}. Total = {soma}')

    if opcao == 'P':
        if resultado_par:
            vitorias += 1
            print('Deu PAR. Você venceu! 😎✨')
            print('Vamos jogar novamente...\n')
        else:
            print('Deu ÍMPAR. Você perdeu! 💀')
            break

    elif opcao == 'I':
        if not resultado_par:
            vitorias += 1
            print('Deu ÍMPAR. Você venceu! 😎✨')
            print('Vamos jogar novamente...\n')
        else:
            print('Deu PAR. Você perdeu! 💀')
            break
print(f'GAME OVER! Você teve {vitorias} vitória(s) consecutiva(s).')