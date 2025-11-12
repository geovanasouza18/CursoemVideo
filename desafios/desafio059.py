num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

opcao = 0
while opcao != 5:
    print('''\nDigite uma dessas opções:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Digite uma dessas opções: '))

    if opcao == 1:
        print(f'A soma dos números {num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'A multipicação dos números {num1} * {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que o {num2}')
        else:
            print(f'O número {num2} é maior que o {num1}')
    elif opcao == 4:
        num1 = int(input('Digite um número inteiro: '))
        num2 = int(input('Digite outro número inteiro: '))
    else:
        print('Saindo do programa...')