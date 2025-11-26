print('\033[33m===== DESAFIO 71 - MUNDO 2 PYTHON =====\033[0m')
print('\033[36m===== BANCO CAIXA =====\033[0m')

valor = int(input('Qual o valor que você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
