salario = float(input("Digite o salario: "))
if salario > 1200:
    aumento = salario + (salario * 10 / 100)
    print("Quem ganhava R${:.2f} passa a ganhar R${}".format(salario, aumento))
else:
    aumento2 = salario + (salario * 15 / 100)
    print("Quem ganhava R${:.2f} passa a ganhar R${}".format(salario, aumento2))
