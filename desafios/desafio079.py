valores = []
while True:
    valor = int(input('Digite um valor: '))
    # Usando o 'if' para verificar a duplicidade
    if valor not in valores:
        valores.append(valor)
        print(f'Valor adicionado com sucesso....')
    else:
        print(f'Valor duplicado na lista. Não vou adicionar.')

    opcao = ' '
    while opcao not in 'SN': #enquanto não for uma dessas opções, vai perguntar eternamente
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
