# #Faça um programa que leia três números e mostre o maior deles:
# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo: '))
# num3 = int(input('Digite o terceiro: '))
# if num1 > num2 and num1 > num3:
#     print(f'O {num1} é o maior número')
# elif num2 > num1 and num2 > num3:
#     print(f'O {num2} é o maior número')
# else:
#     print(f'O {num3} é o maior número')
#
# #Faça um programa que leia três números e mostre o maior e o menor deles:
# number1 = int(input('Digite o primeiro numero: '))
# number2 = int(input('Digite o segundo: '))
# number3 = int(input('Digite o terceiro: '))
# maior = max(number1, number2, number3)
# menor = min(number1, number2, number3)
# print(f'O maior número é {maior} e o menor número é {menor}')
#
# #Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
# prod1 = float(input('Digite o valor do produto: '))
# prod2 = float(input('Digite o valor do produto: '))
# prod3 = float(input('Digite o valor do produto: '))
# menor = min(prod1, prod2, prod3)
# print(f'O produto mais barato e que deve comprar é {menor:.2f}')
#
# #Faça um programa que leia três números e mostre-os em ordem decrescente:
# n1, n2, n3 = map(int, input('Digite três valores: ').split())
# lista = [n1, n2, n3]
# lista.sort(reverse=True)
# print(lista)
#
# #Faça um programa que pergunte em que turno você estuda. Peça para digitar:
# turno = input('Que turno você estuda? (M, V, N) ').upper()[0]
# if turno == 'M':
#     print('Bom dia!')
# elif turno == 'V':
#     print('Boa tarde!')
# elif turno == 'N':
#     print('Boa noite!')
# else:
#     print('Valor Inválido!')
#
# #Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual
# salario: float = float(input('Digite seu salário atual: '))
# print(f'Seu salário é {salario:.2f}')
# if salario <= 280:
#     aumento = (salario * 20 / 100)
#     novo_salario = salario + aumento
#     print('O percentual de aumento aplicado foi de 20%')
#     print(f'O valor do aumento {aumento:.2f}')
#     print(f'Seu salário com aumento deu: {novo_salario:.2f}')
# elif salario > 280 and salario <= 700:
#     aumento = (salario * 15 / 100)
#     novo_salario = salario + aumento
#     print('O percentual de aumento aplicado foi de 15%')
#     print(f'O valor do aumento {aumento:.2f}')
#     print(f'Seu salário com aumento deu: {novo_salario:.2f}')
# elif salario > 700 and salario <= 1500:
#     aumento = (salario * 10 / 100)
#     novo_salario = salario + aumento
#     print('O percentual de aumento aplicado foi de 10%')
#     print(f'O valor do aumento {aumento:.2f}')
#     print(f'Seu salário com aumento deu: {novo_salario:.2f}')
# else:
#     aumento = (salario * 5 / 100)
#     novo_salario = salario + aumento
#     print('O percentual de aumento aplicado foi de 5%')
#     print(f'O valor do aumento {aumento:.2f}')
#     print(f'Seu salário com aumento deu: {novo_salario:.2f}')
#
# #Faça um programa para o cálculo de uma folha de pagamento
# valor_hora, horas = map(float, input('Digite o valor da hora e as horas trabalhadas (ex: 5 220): ').split())
# salario_bruto = valor_hora * horas
# if salario_bruto <= 900:
#     percentual_ir = 0
# elif salario_bruto <= 1500:
#     percentual_ir = 5
# elif salario_bruto <= 2500:
#     percentual_ir = 10
# else:
#     percentual_ir = 20
#
# # Cálculos dos descontos e taxas
# ir = salario_bruto * (percentual_ir / 100)
# inss = salario_bruto * 0.10
# fgts = salario_bruto * 0.11
# total_descontos = ir + inss
# salario_liquido = salario_bruto - total_descontos
#
# # Saída de dados formatada e alinhada
# # :<30 -> Alinha o texto à esquerda em 30 espaços
# # :>10.2f -> Alinha o número à direita em 10 espaços com 2 casas decimais
#
# print("\n" + "="*45)
# print(f"{'Salário Bruto: (' + str(valor_hora) + ' * ' + str(horas) + ')':<30} : R$ {salario_bruto:>10.2f}")
# print(f"{'(-) IR (' + str(percentual_ir) + '%)':<30} : R$ {ir:>10.2f}")
# print(f"{'(-) INSS (10%)':<30} : R$ {inss:>10.2f}")
# print(f"{'FGTS (11%)':<30} : R$ {fgts:>10.2f}")
# print(f"{'Total de descontos':<30} : R$ {total_descontos:>10.2f}")
# print(f"{'Salário Líquido':<30} : R$ {salario_liquido:>10.2f}")
# print("="*45)
#
# #Faça um programa que leia um número e exiba o dia correspondente da semana
# dia = int(input('Digite um número de 1 à 7 para descobrir qual seu dia semana: '))
# if dia == 1:
#     print('Domingo')
# elif dia == 2:
#     print('Segunda')
# elif dia == 3:
#     print('Terça')
# elif dia == 4:
#     print('Quarta')
# elif dia == 5:
#     print('Quinta')
# elif dia == 6:
#     print('Sexta')
# elif dia == 7:
#     print('Sábado')
# else:
#     print('Valor inválido')
#
# #Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
# print('''
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero         E
# ''')
# notas1, notas2 = map(float,input('Digite as duas notas do aluno: ').split())
# media = (notas1 + notas2) / 2
# print(f'As notas do aluno foram {notas1} e {notas2}')
# print(f'A média foi de {media:.2f}')
# if 9.0 <= media <= 10.0:
#     print('A')
#     print('Aprovado')
# elif 7.5 <= media <= 9.0:
#     print('B')
#     print('Aprovado')
# elif 6.0 <= media <= 7.5:
#     print('C')
#     print('Aprovado')
# elif 4.0 <= media <= 6.0:
#     print('D')
#     print('Reprovado')
# else:
#     print('E')
#     print('Reprovado')
#
# #Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# A, B, C = map(int, input('Insira três valores para saber se forma um triângulo: ').split())
# if (A + B > C) and (A + C > B) and (B + C > A):
#     print('Forma um triângulo')
#     if A == B == C:
#         print('Triângulo Equilátero')
#     elif A == B or A == C or B == C:
#         print('Triângulo Isóscele')
#     elif A != B != C:
#         print('Triângulo Escaleno')
# else:
#     print('Não forma um triângulo')
#
# #Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
numero = 0
while True:
    numero = int(input("Digite um numero inteiro: "))
    if 0 < numero <= 10:
        print('Número válido')
        break
    else:
        print('Número inválido! Tente novamente')
