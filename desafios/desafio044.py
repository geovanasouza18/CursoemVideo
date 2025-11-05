import time

valor_produto = float(input('Digite o valor do produto: R$'))
print("\033[33mBem-vindo ao Menu de Investigação\033[0m")
print("\033[36m🧾 Opção 1 – À vista dinheiro/cheque (10% de desconto)\033[0m")
print("\033[35m💳 Opção 2 – À vista no cartão (5% de desconto)\033[0m")
print("\033[32m📍 Opção 3 – 2x no cartão (preço normal)\033[0m")
print("\033[31m💥 Opção 4 – 3x ou mais no cartão (20% de juros)\033[0m")
opcao = input("Escolha a operação (1/2/3/4): ")

print("\033[33mProcessando...\033[0m")
time.sleep(2)

if opcao == "1":
    print('Pagamento à vista em dinheiro/cheque selecionado. \nVocê recebeu 10% de desconto! 🎉')
    dinheiro = valor_produto - (valor_produto * 0.10)
    print('Processando o pagamento...')
    time.sleep(2)
    print(f"\033[36mO valor com desconto: R$ {dinheiro:.2f}\033[0m")

elif opcao == "2":
    print('Pagamento à vista no cartão selecionado. \nVocê recebeu 5% de desconto! 🎉')
    cartao = valor_produto - (valor_produto * 0.05)
    print('Processando o pagamento...')
    time.sleep(2)
    print(f"\033[35mO valor de R$ {valor_produto:.2f} caiu para R$ {cartao:.2f}.\033[0m")

elif opcao == "3":
    print('Pagamento em 2x no cartão selecionado.\nSem desconto ou juros. 🙂')
    parcelado_duas = valor_produto / 2
    print('Processando o pagamento...')
    time.sleep(2)
    print(f"\033[32mSua compra será dividida em 2 parcelas de R$ {parcelado_duas:.2f}.\033[0m")

elif opcao == "4":
    parcelas = int(input('Digite a quantidade de parcelas (3 ou mais): '))
    print('Pagamento parcelado em 3x ou mais no cartão selecionado.\nAtenção: será aplicado 20% de juros. 💸')
    parcelado_tres = valor_produto + (valor_produto * 0.20)
    dividido = parcelado_tres / parcelas
    print('Processando o pagamento...')
    time.sleep(2)
    print(f'Sua compra será parcelada em {parcelas}x de R$ {dividido:.2f}.\nTotal com juros: R$ {parcelado_tres:.2f}.')

else:
    print('\033[31mOpção inválida! Tente novamente. ⚠️\033[0m')
