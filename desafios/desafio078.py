valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

maior = max(valores)
menor = min(valores)

# listas para guardar todas as posições
posicaoMaior = []
posicaoMenor = []

# percorre a lista inteira e coleta as posições
for posicao, valor in enumerate(valores):
    if valor == maior:
        posicaoMaior.append(posicao)
    if valor == menor:
        posicaoMenor.append(posicao)

print(f'Você digitou os valores {valores}')
print(f'O maior número foi {maior} nas posições {posicaoMaior}')
print(f'O menor número foi {menor} nas posições {posicaoMenor}')
