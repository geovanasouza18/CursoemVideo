quant = maior_peso = menor_peso = 0
galera = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    quant += 1

    opcao = ' '
    while opcao not in 'SN': #enquanto não for uma dessas opções, vai perguntar eternamente
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break

peso_max = max(pessoa[1] for pessoa in galera)
peso_min = min(pessoa[1] for pessoa in galera)

print(f'Ao todo, você cadastrou {quant} pessoas.')

print(f'O maior peso foi de {peso_max}Kg. Peso de ', end='')
for pessoa in galera:
    if pessoa[1] == peso_max:
        print(pessoa[0], end=' ')


print(f'\nO menor peso foi de {peso_min}Kg. Peso de ', end='')
for pessoa in galera:
    if pessoa[1] == peso_min:
        print(pessoa[0], end=' ')


