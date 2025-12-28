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

