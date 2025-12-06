lista = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N] ').strip().upper()
    if opcao == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
