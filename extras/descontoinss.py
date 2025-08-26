salario = float(input("Digite seu salário: R$ "))

if salario <= 1518:
    novo = salario - (salario * 7.5 / 100)
    print("O salário com desconto do INSS é: R${:.2f}".format(novo))

elif salario > 1518 and salario <= 2793.88:
    novo = salario - (salario * 9 / 100)
    print("O salário com desconto do INSS é: R${:.2f}".format(novo))

elif salario > 2793.88 and salario <= 4190.83:
    novo = salario - (salario * 12 / 100)
    print("O salário com desconto do INSS é: R${:.2f}".format(novo))

else:
    novo = salario - (salario * 14 / 100)
    print("O salário com desconto do INSS é: R${:.2f}".format(novo))
