"""vel = float(input("Qual a velocidade do seu carro?: "))
multa = (vel - 80) * 7
if vel > 80:
    print("Sua velocidade foi multado em R$ {:.2f}".format(multa))
else:
    print("Você não ultrapassou a velocidade")
"""
#Desafio feio pelo Prof Guanabara
velocidade = float(input("Qual a velocidade do seu carro?: "))
if velocidade > 80:
    print("MULTADO! Você excedeu o limite de velocidade de 80km/h")
    multa = (velocidade - 80) * 7
    print("Você deve pagar uma multa de R${:.2f}".format(multa))

print("Tenha um bom dia! Dirija com segurança")