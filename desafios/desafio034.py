salario = float(input("Digite o salario: "))
aumento = salario * 0.10
aumento2 = salario * 0.15
if salario > 1200:
    print("Seu aumento foi de R${}".format(aumento))
else:
    print("Seu aumento foi de R${}".format(aumento2))
