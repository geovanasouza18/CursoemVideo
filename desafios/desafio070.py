print('\033[33m===== DESAFIO 70 - MUNDO 2 PYTHON =====\033[0m')
print('\033[34m===== LOJÃO DO BARATÃO =====\033[0m')

total = quant = maisBaratoValor = maisBaratoNome = 0
while True:
    nomeProduto = str(input('Nome do produto: '))
    valorProduto = float(input('Valor do produto: '))
    total += valorProduto

    if valorProduto > 1000:
        quant +=1
    if total == valorProduto:
        maisBaratoValor = valorProduto
        maisBaratoNome = nomeProduto
    elif valorProduto < maisBaratoValor:
        maisBaratoValor = valorProduto
        maisBaratoNome = nomeProduto
    opcao = ' '
    while opcao not in 'SN':  # enquanto não for uma dessas opções, vai perguntar eternamente
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        print('-------------- FIM DO PROGRAMA ---------------')
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {quant} produtos custando mais de um R$1.000,00')
print(f'O produto mais barato foi {maisBaratoNome} que custa R${maisBaratoValor:.2f}')