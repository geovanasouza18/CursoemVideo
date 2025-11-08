from datetime import date

for ano in range(0, 7):
    idade = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year - idade
    if atual >= 21