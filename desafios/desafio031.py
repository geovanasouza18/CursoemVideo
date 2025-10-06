distancia = float(input("Digite a distância da sua viagem: "))
valor = distancia * 0.50
valor2 = distancia * 0.45
if distancia <= 200:
    print("Sua passagem custou R${:.2f}".format(valor))
else:
    print("Sua passagem custou R${:.2f}".format(valor2))