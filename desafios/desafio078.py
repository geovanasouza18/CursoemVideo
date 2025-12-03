valores =list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    maior = max(valores)
    menor = min(valores)
print(f'Você digitou os valores {valores}')

print(f'O maior número foi {maior} nas posições ')
print(f'O menor número foi {menor} nas posições ')
