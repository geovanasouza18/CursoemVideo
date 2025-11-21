number = 0
soma = 0
total = 0
while number != 999:
    number = int(input('Digite um número inteiro (ou 999 para sair): '))
    if number != 999:
        soma += number
        total += 1
print(f'A soma dos números foi {soma} e os números foram digitados {total} vezes')
