vel = float(input("Qual a velocidade do seu carro?: "))
multa = (vel - 80) * 7
if vel > 80:
    print("Sua velocidade foi multado em R$ {:.2f}".format(multa))
else:
    print("Você não ultrapassou a velocidade")
