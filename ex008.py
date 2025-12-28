#Faça um programa que leia três números e mostre o maior deles:
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo: '))
num3 = int(input('Digite o terceiro: '))
if num1 > num2 and num1 > num3:
    print(f'O {num1} é o maior número')
elif num2 > num1 and num2 > num3:
    print(f'O {num2} é o maior número')
else:
    print(f'O {num3} é o maior número')

#Faça um programa que leia três números e mostre o maior e o menor deles:
number1 = int(input('Digite o primeiro numero: '))
number2 = int(input('Digite o segundo: '))
number3 = int(input('Digite o terceiro: '))
maior = max(number1, number2, number3)
menor = min(number1, number2, number3)
print(f'O maior número é {maior} e o menor número é {menor}')

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
prod1 = float(input('Digite o valor do produto: '))
prod2 = float(input('Digite o valor do produto: '))
prod3 = float(input('Digite o valor do produto: '))
menor = min(prod1, prod2, prod3)
print(f'O produto mais barato e que deve comprar é {menor:.2f}')

#Faça um programa que leia três números e mostre-os em ordem decrescente:
n1, n2, n3 = map(int, input('Digite três valores: ').split())
lista = [n1, n2, n3]
lista.sort(reverse=True)
print(lista)

#Faça um programa que pergunte em que turno você estuda. Peça para digitar:
turno = input('Que turno você estuda? (M, V, N) ').upper()[0]
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')

