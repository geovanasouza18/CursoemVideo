num = int(input('Digite um número inteiro: '))
print('''Digite uma dessas opções:
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
opcao = int(input('Sua escolha: '))
if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida')