termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
for resultado in range(10):
    print(termo, end=' → ')
    termo += razao
print('ACABOU!')

#COMO O PROF GAUANABARA FEZ
primeiro = int(input('Digite o primeiro termo: '))
razao2 = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao2
for c in range(primeiro, decimo + razao2, razao2):
    print(c , end=' → ')
print('ACABOU!')