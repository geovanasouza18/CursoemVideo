print('\033[33m===== DESAFIO 69 - MUNDO 2 PYTHON =====\033[0m')
const = homens = mulheres = 0

while True:
    print('\033[33m===== CADASTRAR UMA PESSOA =====\033[0m')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idade > 18:
        const += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()
    if opcao == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {const}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')
