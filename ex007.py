#CASO 01 — O Cofre do Sr. Holmes
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(f'A soma dos números {num1} + {num2} = {num1 + num2}')
print(f'A subtração dos números {num1} - {num2} = {num1 - num2}')
print(f'A multiplicação dos números {num1} * {num2} = {num1 * num2}')
print(f'A divisão dos números {num1} / {num2} = {num1 / num2:.2f}')

# Caso 02 — O Cliente Misterioso
const = 0
while True:
    preco = int(input('Digite um valor: '))
    if preco < 0:
        break
    const += preco

print(f'O total da soma dos números foi: {const}')