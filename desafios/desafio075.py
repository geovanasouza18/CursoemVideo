A, B, C, D = map(int, input('Digite 4 valores: ').split())
tupla = (A, B, C, D)

print(f'Você digitou os valores: {tupla}')

count9 = tupla.count(9)
print(f'O valor 9 apareceu {count9} vezes')

if 3 in tupla:
    num3 = tupla.index(3)
    print(f'O valor 3 apareceu na {num3 + 1}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')