number = 1
soma = 0
total = 0
maior = None
menor = None

while number != 0:
    number = int(input('Digite um número inteiro ou 0 para sair: '))

    if number != 0:
        soma += number
        total += 1

        if maior is None or number > maior:
            maior = number
        if menor is None or number < menor:
            menor = number

media = soma / total

print(f'O maior número foi {maior} e o menor foi {menor}')
print(f'A média dos números foi {media:.2f}')
