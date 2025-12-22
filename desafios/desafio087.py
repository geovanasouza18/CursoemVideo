#desafio 86 - Matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma_linha = maior_linha2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

#Mostrar a matriz de forma organizada
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print([matriz[l][c]], end=' ')
    print()

#Somar as matrizes
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

#Soma da terceira coluna
for l in range(len(matriz)):
    if matriz[l][2]:
        soma_linha += matriz[l][2]

maior_linha2 = max(matriz[1])

print(f'A soma dos pares é {soma}')
print(f'A soma  dos valores da terceira coluna é {soma_linha}')
print(f'O maior valor da segunda linha é {maior_linha2}')
