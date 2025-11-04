import time
print('\033[34m=======🕵️‍♀️ Bem-vindo ao Departamento de Investigações Financeiras de Baker Street!=======\033[m')
valor_casa = float(input('Quanto vale a casa dos seus sonhos? (somente números) R$'))
salario = float(input('Qual é a renda mensal do suspeito... digo, comprador? (somente números) '))
anos_pagamento = int(input('Em quantos anos ele planeja quitar a dívida? '))

#cálculos
prestacao = valor_casa / (anos_pagamento * 12)
limite = salario * 0.3

time.sleep(1)
print('⏳ Processando... (respira, não pira)')
time.sleep(2)

if prestacao <= limite:
    print('\033[33mAPROVADO! — Pode comprar seu lar doce lar!\033[m')
else:
    print('\033[31mNEGADO! A prestação ultrapassa o limite e isso seria um crime financeiro!\033[m')