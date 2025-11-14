termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
contador = 0
termos = 10
while contador < 10:
    print(f'{termo} ', end = '-> ' )
    termo = termo + razao
    contador += 1

print('FIM')