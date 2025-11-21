#Como Guanabara fez
resp = 'Ss'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / quant
print(f'O maior número foi {maior} e o menor foi {menor}')
print(f'A média dos números foi {media:.2f}')