valores = []
pares = []
impares = []
for num in range(1, 8):
    num = (int(input(f'Digite o {num}º valor: ')))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'Os valores pares digitados foram {sorted(pares)}')
print(f'Os valores impares digitados foram {sorted(impares)}')