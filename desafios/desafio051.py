termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for resultado in range(10):
    print(termo, end=' → ')
    termo += razao
