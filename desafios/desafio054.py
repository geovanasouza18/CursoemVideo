from datetime import date

maiores = 0
menores = 0

for pessoa in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - nascimento

    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'\nAo todo tivemos {maiores} pessoas maiores de idade.')
print(f'E também tivemos {menores} pessoas menores de idade.')
