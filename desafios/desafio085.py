valores = []
pares = []
impares = []
for num in range(1, 8):
    valores.append(int(input(f'Digite o {num}º valor: ')))
if valores % 2 == 0:
    pares.append(valores[:])
else:
    impares.append(valores[:])
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')