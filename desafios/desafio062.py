termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
contador = 0
mais_termos = 10
total = 0

while mais_termos != 0:
    total += mais_termos
    while contador < total:
        print(f'{termo}', end=' -> ')
        termo += razao
        contador += 1
    print('Pausa')
    mais_termos = int(input('Quantos termos você quer mostrar mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
